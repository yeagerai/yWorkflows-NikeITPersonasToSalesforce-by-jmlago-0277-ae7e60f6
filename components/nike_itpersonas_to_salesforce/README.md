
# NikeITPersonasToSalesforce

This is a Yeager workflow component that takes organization name, department name, and Salesforce credentials as input.
It processes the information and stores it into the Salesforce platform. It returns the number of successful imports
and the total number of records imported as output.


## Initial generation prompt
description: 'IOs - InputBaseModel:

  - organization_name: str

  - department_name: str

  - salesforce_credentials: Dict[str, Any]

  OutputBaseModel:

  - successful_imports: int

  - total_imported: int

  '
name: NikeITPersonasToSalesforce


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        