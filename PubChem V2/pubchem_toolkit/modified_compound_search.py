# File: pubchem_toolkit/compound_search.py

import requests
import logging

logging.basicConfig(level=logging.INFO)


def autocomplete_search(query, dictionary, limit=10):
    """
    Perform auto-complete search using PubChem REST auto-complete API.

    Args:
        query (str): Search query.
        dictionary (str): Dictionary to search in (e.g., 'compound', 'gene', 'taxonomy', 'assay').
        limit (int): Maximum number of returned results (default is 10).

    Returns:
        list: List of suggested terms matching the query.
    """
    base_url = (
        f"https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/{dictionary}/{query}/json"
    )
    params = {"limit": limit}

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "dictionary_terms" in data:
            return data["dictionary_terms"][dictionary]
        else:
            return []
    else:
        raise Exception(
            "Failed to perform auto-complete search. Check your query and try again."
        )


def get_compound_properties_with_autocomplete(
    identifier, identifier_type="name", property_name=None
):
    """
    Retrieve compound properties or a specific compound property from PubChem API based on compound identifier.
    This function first performs an auto-complete search to get a suggested compound name based on the input identifier.
    Then, it retrieves the compound properties for the suggested compound.

    Args:
        identifier (str): Identifier of the compound (e.g., name, CID, SMILES, InChI, SDF, InChIKey, formula).
        identifier_type (str, optional): Type of the identifier. Defaults to "name".
        property_name (str, optional): Name of the property to retrieve. If not provided, all properties are returned.

    Returns:
        dict or str or int or float: Dictionary containing all compound properties if property_name is None,
            or value of the specified compound property.
    """
    try:
        suggested_compound = autocomplete_search(identifier, "compound", limit=1)
        if suggested_compound:
            suggested_identifier = suggested_compound[0]
            base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/{}/json"
            url = base_url.format(identifier_type + "/" + suggested_identifier)

            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad status codes
            data = response.json()
            properties = data["PC_Compounds"][0]["props"]
            if property_name:
                for prop in properties:
                    label = prop["urn"]["label"]
                    if label == property_name:
                        if "sval" in prop["value"]:
                            return prop["value"]["sval"]
                        elif "ival" in prop["value"]:
                            return prop["value"]["ival"]
                        elif "fval" in prop["value"]:
                            return prop["value"]["fval"]
                        else:
                            return None
                logging.warning(
                    "Property '%s' not found for compound with %s '%s'",
                    property_name,
                    identifier_type,
                    suggested_identifier,
                )
                return None
            else:
                compound_properties = {}
                for prop in properties:
                    label = prop["urn"]["label"]
                    if "sval" in prop["value"]:
                        value = prop["value"]["sval"]
                    elif "ival" in prop["value"]:
                        value = prop["value"]["ival"]
                    elif "fval" in prop["value"]:
                        value = prop["value"]["fval"]
                    else:
                        value = None
                    compound_properties[label] = value
                return compound_properties
        else:
            logging.warning(
                "No suggested compound found for the identifier '%s'", identifier
            )
            return None
    except Exception as e:
        logging.error("Failed to retrieve compound properties: %s", str(e))
        raise
