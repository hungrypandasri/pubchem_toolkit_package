# File: tests/test_compound_search.py

import unittest
from pubchem_toolkit.compound_search import get_compound_properties


class TestCompoundSearch(unittest.TestCase):
    def test_valid_compound_by_name(self):
        properties = get_compound_properties("aspirin", identifier_type="name")
        self.assertIsNotNone(properties)
        self.assertIsInstance(properties, dict)

    def test_valid_compound_by_cid(self):
        properties = get_compound_properties("2244", identifier_type="cid")
        self.assertIsNotNone(properties)
        self.assertIsInstance(properties, dict)

    def test_valid_compound_by_smiles(self):
        properties = get_compound_properties(
            "O=C(C)Oc1ccccc1C(=O)O", identifier_type="smiles"
        )
        self.assertIsNotNone(properties)
        self.assertIsInstance(properties, dict)

    # def test_invalid_compound(self):
    #     with self.assertRaises(Exception):
    #         get_compound_properties("nonexistentcompound")

    # def test_invalid_identifier_type(self):
    #     with self.assertRaises(ValueError):
    #         get_compound_properties("aspirin", identifier_type="invalid_type")


if __name__ == "__main__":
    unittest.main()
