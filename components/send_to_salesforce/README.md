markdown
# Component Name

SendToSalesforce

# Description

The SendToSalesforce component is a building block of a Yeager Workflow designed to send a list of names and emails to Salesforce using the Salesforce API. It handles authentication, iterates through the input list, and sends each name and email in a structured format to Salesforce.

# Input and Output Models

## Input: SendToSalesforceInputDict

- `name_email_list`: a list of dictionaries, where each dictionary contains a `str` key-value pair for the name and email.
- `salesforce_credentials`: a dictionary containing the necessary authentication information for the Salesforce API.

Example:

