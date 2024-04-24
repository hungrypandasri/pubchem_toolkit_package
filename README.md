# PubChem Toolkit V0.0.2

The PubChem Toolkit is a Python package that provides a convenient wrapper around the PubChem PUG REST API. It simplifies the process of searching for compound properties available at PubChem, allowing users to retrieve information about chemical compounds using their names, molecular formulas, or SMILES notation.

## Installation

You can install the PubChem Toolkit via pip. Open a terminal or command prompt and run the following command:

```bash
pip install pubchem_toolkit

## Usage

### Auto-Complete Search

The `autocomplete_search` function performs auto-complete search using the PubChem REST auto-complete API. It takes three parameters: `query`, `dictionary`, and `limit`.

```python
from pubchem_toolkit.compound_search import autocomplete_search

suggestions = autocomplete_search("aspirin", "compound", limit=5)
print(suggestions)

### Retrieving Compound Properties

The `get_compound_properties_with_autocomplete` function retrieves compound properties or a specific compound property from the PubChem API based on the compound identifier. It first performs an auto-complete search to get a suggested compound name based on the input identifier.

#### Parameters:

- `identifier`: Identifier of the compound (e.g., name, CID, SMILES, InChI, SDF, InChIKey, formula).
- `identifier_type` (optional): Type of the identifier. Defaults to "name".
- `property_name` (optional): Name of the property to retrieve. If not provided, all properties are returned.

#### Returns:

- Dictionary containing all compound properties if `property_name` is None, or value of the specified compound property.

```python
from pubchem_toolkit.compound_search import get_compound_properties_with_autocomplete

# Retrieve all properties for a compound by name
compound_properties = get_compound_properties_with_autocomplete("aspirin")
print(compound_properties)

# Retrieve a specific property (e.g., Molecular Formula) for a compound by CID
molecular_formula = get_compound_properties_with_autocomplete(2244, identifier_type="cid", property_name="MolecularFormula")
print(molecular_formula)

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on GitHub or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
