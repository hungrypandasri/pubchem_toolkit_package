# PubChem Toolkit

The PubChem Toolkit is a Python package, convenient wrapper around PubChem PUG REST API that allows to search for many compound properties available at PubChem with ease. It allows users to retrieve information about chemical compounds using their names, molecular formulas, or SMILES notation.

## Installation

You can install the PubChem Toolkit via pip. Open a terminal or command prompt and run the following command:

```bash
pip install pubchem_toolkit

## Usage

### Retrieving Compound Properties

To retrieve properties for a compound, you can use the `get_compound_properties` function. This function takes three parameters: `identifier`, `identifier_type`, and `property_name`.

- `identifier`: The identifier of the compound. It could be the compound name, CID, SMILES notation, InChI, SDF, InChIKey, or formula.
- `identifier_type` (optional): Type of the identifier. Defaults to "name". Supported types include `cid`, `name`, `smiles`, `inchi`, `sdf`, `inchikey`, and `formula`.
- `property_name` (optional): Name of the property to retrieve. If not provided, all properties are returned.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on GitHub or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

