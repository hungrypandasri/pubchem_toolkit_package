# File: tests_pytest/test_compound_search.py

import pytest
from pubchem_toolkit.modified_compound_search import autocomplete_search
from pubchem_toolkit.modified_compound_search import get_compound_properties_with_autocomplete


def test_valid_autocomplete_search():
    compounds = autocomplete_search("aspirin", dictionary="compound", limit=6)
    assert compounds is not None
    assert isinstance(compounds, list)
    assert len(compounds) > 0


def test_invalid_autocomplete_search():
    invalid_result = autocomplete_search(
        "nonexistentquery", dictionary="compound", limit=10
    )
    assert invalid_result == []


def test_valid_compound_search():
    properties = get_compound_properties_with_autocomplete("aspirin")
    assert properties is not None
    assert isinstance(properties, dict)


def test_invalid_compound_search():
    with pytest.raises(Exception):
        get_compound_properties_with_autocomplete("nonexistentcompound")
