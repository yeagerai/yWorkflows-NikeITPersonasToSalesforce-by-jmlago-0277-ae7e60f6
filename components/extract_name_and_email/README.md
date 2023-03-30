
# ExtractNameAndEmail

Extracts the name and email for each persona if available from the persona_list provided. Outputs a list of dictionaries containing name and email.

## Initial generation prompt
description: Extracts the name and email for each persona if available from the persona_list
  provided. Outputs a list of dictionaries containing name and email.
inputs:
- persona_list: List[Dict[str, Any]]
name: ExtractNameAndEmail
outputs:
- name_email_list: List[Dict[str, str]]


## Transformer breakdown
- Initialize an empty list named 'result'
- Iterate through the persona_list
- For each persona, check if the name and email keys exist
- If both keys exist, create a dictionary containing name and email with keys 'name' and 'email'
- Add the dictionary to the 'result' list
- Return the 'result' list as the output

## Parameters
[]

        