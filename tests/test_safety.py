import json, sys, os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from safety import classify_glucose

data = json.load(open("data/cases_v1.json"))
assert data["schema_version"] == "1"

@pytest.mark.parametrize("c", data["cases"], ids=lambda c: c["id"])
def test_case(c):
    assert classify_glucose(c["value"], c["unit"]) == c["expected"]