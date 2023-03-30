
# test_send_to_salesforce.py

import pytest
from pydantic import BaseModel
from typing import List, Dict, Any

from components.send_to_salesforce import SendToSalesforce, SendToSalesforceInputDict, SendToSalesforceOutputDict


# Create an instance of the component
send_to_salesforce = SendToSalesforce()

# Mocked data examples
input_data1 = SendToSalesforceInputDict(
    name_email_list=[{"name": "John Smith", "email": "john@example.com"}],
    salesforce_credentials={"api_key": "12345"},
)

expected_output_data1 = SendToSalesforceOutputDict(
    successful_imports=1,
    total_imported=1
)

input_data2 = SendToSalesforceInputDict(
    name_email_list=[{"name": "John Smith", "email": "john@example.com"},
                     {"name": "Jane Smith", "email": "jane@example.com"}],
    salesforce_credentials={"api_key": "12345"},
)

expected_output_data2 = SendToSalesforceOutputDict(
    successful_imports=2,
    total_imported=2
)

# Define test cases and expected output using @pytest.mark.parametrize
@pytest.mark.parametrize("input_data, expected_output_data", [
    (input_data1, expected_output_data1),
    (input_data2, expected_output_data2),
])
def test_send_to_salesforce_transform(input_data: SendToSalesforceInputDict,
                                      expected_output_data: SendToSalesforceOutputDict):
    # Call transform() method with mocked input data
    result = send_to_salesforce.transform(input_data)

    # Assert that the output data matches the expected output data
    assert result == expected_output_data

