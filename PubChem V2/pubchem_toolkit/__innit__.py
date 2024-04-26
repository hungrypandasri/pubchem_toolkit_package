"""
PubChem Toolkit: A toolkit for accessing PubChem database.

This module provides functions for interacting with the PubChem database.
"""

# Import commonly used modules or functions
from .modified_compound_search import autocomplete_search, get_compound_properties_with_autocomplete

# Export the functions to make them available when importing the package
__all__ = ["autocomplete_search", "get_compound_properties_with_autocomplete"]
