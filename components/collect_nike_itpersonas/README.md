
# CollectNikeITPersonas

Retrieves a list of personas belonging to IT department at Nike. Assumes access to an API or database with this information. Takes organization_name and department_name as inputs and outputs persona_list.

## Initial generation prompt
description: Retrieves a list of personas belonging to IT department at Nike. Assumes
  access to an API or database with this information. Takes organization_name and
  department_name as inputs and outputs persona_list.
inputs:
- organization_name: str
- department_name: str
name: CollectNikeITPersonas
outputs:
- persona_list: List[Dict[str, Any]]


## Transformer breakdown
- Verify inputs are valid (organization_name and department_name)
- Use API/database access to query personas for the specified organization and department
- Retrieve and store the result as persona_list
- Return persona_list

## Parameters
[]

        