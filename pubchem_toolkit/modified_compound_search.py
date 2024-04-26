# Utility function of package

import requests
import logging

logging.basicConfig(level=logging.INFO)


def get_compound_properties(identifier, identifier_type="name", property_name=None):
    """
    Retrieve compound properties or a specific compound property from PubChem API based on compound identifier.

    Args:
        identifier (str): Identifier of the compound (e.g., name, CID, SMILES, InChI, SDF, InChIKey, formula).
        identifier_type (str, optional): Type of the identifier. Defaults to "name".
        property_name (str, optional): Name of the property to retrieve. If not provided, all properties are returned.

    Returns:
        dict or str or int or float: Dictionary containing all compound properties if property_name is None,
            or value of the specified compound property.
    """
    if not identifier:
        raise ValueError("Identifier cannot be empty")

    if identifier_type not in [
        "cid",
        "name",
        "smiles",
        "inchi",
        "sdf",
        "inchikey",
        "formula",
    ]:
        raise ValueError(
            "Invalid identifier type. Supported types: cid, name, smiles, inchi, sdf, inchikey, formula"
        )

    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/{}/json"
    url = base_url.format(identifier_type + "/" + identifier)

    try:
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
                identifier,
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
    except requests.exceptions.RequestException as e:
        logging.error("Failed to retrieve compound properties: %s", str(e))
        raise
    except (KeyError, IndexError):
        logging.error(
            "Compound properties not found for %s '%s'", identifier_type, identifier
        )
        raise Exception(
            "Compound properties not found. Check compound identifier and try again."
        )
