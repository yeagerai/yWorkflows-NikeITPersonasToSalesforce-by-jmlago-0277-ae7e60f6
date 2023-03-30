
import pytest
from pydantic import ValidationError
from typing import Dict, List, Any

from component_path import ExractNameAndEmail, ExtractNameAndEmailInputDict, ExtractNameAndEmailOutputDict

# Define test cases with mocked input and expected output data
test_data = [
    (
        {"persona_list": [{"name": "John", "email": "john@example.com"}]},
        {"name_email_list": [{"name": "John", "email": "john@example.com"}]},
    ),
    (
        {"persona_list": [{"name": "John", "email": "john@example.com"}, {"phone": "1234567890"}]},
        {"name_email_list": [{"name": "John", "email": "john@example.com"}]},
    ),
    (
        {"persona_list": [{"phone": "1234567890"}]},
        {"name_email_list": []},
    ),
    (
        {"persona_list": []},
        {"name_email_list": []},
    ),
]

# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output_data", test_data)
def test_extract_name_and_email_transform(input_data: Dict[str, Any], expected_output_data: Dict[str, Any]):

    # Create an instance of the ExtractNameAndEmail component
    extract_name_and_email = ExtractNameAndEmail()

    # Create input and output objects using input data and expected output data
    extract_name_and_email_input = ExtractNameAndEmailInputDict(**input_data)
    expected_output = ExtractNameAndEmailOutputDict(**expected_output_data)

    # Call the component's transform() method with the input object
    output = extract_name_and_email.transform(extract_name_and_email_input)

    # Assert that the output matches the expected output
    assert output == expected_output

# Error handling and edge case scenarios
def test_transform_with_invalid_input():

    # Create an instance of the ExtractNameAndEmail component
    extract_name_and_email = ExtractNameAndEmail()

    with pytest.raises(ValidationError):
        try:
            # Pass an invalid input object
            extract_name_and_email_input = ExtractNameAndEmailInputDict(persona_list="not a list")

            # Call the component's transform() method with the input object
            extract_name_and_email.transform(extract_name_and_email_input)

        except ValidationError as e:
            print(str(e))
            raise ValidationError from e

    with pytest.raises(ValidationError):
        try:
            # Pass an input object with the wrong field name
            extract_name_and_email_input = ExtractNameAndEmailInputDict(wrong_field=[{"name": "John", "email": "john@example.com"}])

            # Call the component's transform() method with the input object
            extract_name_and_email.transform(extract_name_and_email_input)

        except ValidationError as e:
            print(str(e))
            raise ValidationError from e
