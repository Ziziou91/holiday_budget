"""Tests for fctns in unit_functions."""
import pytest
from unit_functions import load_json

def test_load_json_returns_dictionary():
    """ensures that load_json returns a dictionary"""
    assert isinstance(load_json("cities.json"), dict)

def test_load_json_FileNotFoundError_error():
    with pytest.raises(FileNotFoundError) as excinfo:
        load_json("test")
    assert str(excinfo.value) == "Error! test is an invalid path."