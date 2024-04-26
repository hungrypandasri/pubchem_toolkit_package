"""Unit tests for compound search functionality."""

import unittest
from pubchem_toolkit.modified_compound_search import autocomplete_search
# from pubchem_toolkit.modified_compound_search import get_compound_properties_with_autocomplete


class TestAutocomplete(unittest.TestCase):
    def test_valid_autocomplete(self):
        # Test auto-complete search for compounds
        compounds = autocomplete_search("aspirin", dictionary="compound", limit=6)
        self.assertIsNotNone(compounds)
        self.assertIsInstance(compounds, list)
        self.assertTrue(len(compounds) > 0)

        # Test auto-complete search for genes
        genes = autocomplete_search("egfr", dictionary="gene", limit=5)
        self.assertIsNotNone(genes)
        self.assertIsInstance(genes, list)
        self.assertTrue(len(genes) > 0)

        # Add more tests for other dictionaries (e.g., assays, taxonomy) if needed

    def test_invalid_autocomplete(self):
        # Test auto-complete search with invalid query
        invalid_result = autocomplete_search(
            "nonexistentquery", dictionary="compound", limit=10
        )
        self.assertEqual(invalid_result, [])


if __name__ == "__main__":
    unittest.main()
