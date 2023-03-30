
# test_nike_it_personas_to_salesforce.py
import typing
from typing import Dict, Any
import pytest
from pydantic import BaseModel
from .nike_it_personas_to_salesforce import (
    NikeITPersonasToSalesforce,
    NikeITPersonasToSalesforceIn,
    NikeITPersonasToSalesforceOut,
)

# Mocked input and output data for test cases
test_data = [
    (
        {
            "organization_name": "Nike",
            "department_name": "IT",
            "salesforce_credentials": {"username": "user", "password": "password"},
        },
        {"successful_imports": 5, "total_imported": 5},
    ),
    (
        {
            "organization_name": "Nike",
            "department_name": "Marketing",
            "salesforce_credentials": {"username": "user", "password": "password"},
        },
        {"successful_imports": 3, "total_imported": 4},
    ),
]

# Test function
@pytest.mark.parametrize("input_data, expected_output", test_data)
async def test_transform(input_data: Dict[str, Any], expected_output: Dict[str, int]):
    # Initialize the component
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()

    # Call the transform() method with mocked input
    input_model = NikeITPersonasToSalesforceIn(**input_data)
    output = await nike_it_personas_to_salesforce.transform(input_model, callbacks=None)

    # Assert that the output matches the expected output
    assert output == NikeITPersonasToSalesforceOut(**expected_output)

