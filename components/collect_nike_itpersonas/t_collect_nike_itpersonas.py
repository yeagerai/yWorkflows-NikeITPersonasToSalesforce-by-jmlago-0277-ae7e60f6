
import pytest
from typing import Any, Dict, List

from components.collect_nike_it_personas import (
    CollectNikeITPersonas,
    CollectNikeITPersonasInputDict,
    CollectNikeITPersonasOutputDict,
)

test_data = [
    (
        CollectNikeITPersonasInputDict(
            organization_name="Nike", department_name="IT"
        ),
        CollectNikeITPersonasOutputDict(
            persona_list=[
                {"name": "John Doe", "role": "IT Manager"},
                {"name": "Jane Smith", "role": "IT Analyst"},
            ]
        ),
    ),
    (
        CollectNikeITPersonasInputDict(
            organization_name="InvalidOrg", department_name="InvalidDept"
        ),
        CollectNikeITPersonasOutputDict(persona_list=[]),
    ),
]

@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_collect_nike_it_personas(input_data: CollectNikeITPersonasInputDict, expected_output: CollectNikeITPersonasOutputDict):
    collect_nike_it_personas = CollectNikeITPersonas()
    output = collect_nike_it_personas.transform(input_data)
    assert output == expected_output

# Add additional tests for error handling and edge case scenarios if applicable
