markdown
# Component Name
CollectNikeITPersonas

# Description
The CollectNikeITPersonas component is designed to query IT personas from a specified organization and department, returning a list of personas with their names and roles.

# Input and Output Models

## Input Model
The component expects an input model of type `CollectNikeITPersonasInputDict`, containing the following properties:

- `organization_name` (str): The name of the organization where IT personas are being collected
- `department_name` (str): The name of the department within the organization

## Output Model
The component returns an output model of type `CollectNikeITPersonasOutputDict`, containing the following properties:

- `persona_list` (List[Dict[str, Any]]): A list of dictionaries where each dictionary represents an IT persona with the keys "name" and "role"

# Parameters
The CollectNikeITPersonas component does not take any parameters during initialization.

# Transform Function

The `transform()` method of the CollectNikeITPersonas component is implemented with the following steps:

1. Validate the `organization_name` and `department_name` supplied in the input model
2. Query the API or database to retrieve personas for the given organization and department (Here, a mock dataset is used as an example)
3. Return the list of personas in a `CollectNikeITPersonasOutputDict` output model

# External Dependencies
This component relies on the following external libraries:

- `os`: to manage file system and environment variables
- `typing`: for type annotations
- `yaml`: to parse YAML configuration files
- `dotenv`: to load environment variables from `.env` files
- `fastapi`: to create the FastAPI web application
- `pydantic`: to define and validate input and output models

# API Calls
This implementation does not include direct API calls, but it is assumed that the persona list is queried from an external API or database. Users should replace the example persona list with their desired API or database call.

# Error Handling
The component relies on FastAPI and Pydantic for error handling and validation of input data. In case the input data does not match the expected input model, an error will be thrown and returned to the client.

# Examples

Here is an example of how to use the CollectNikeITPersonas component in a Yeager Workflow:

1. Create a FastAPI app instance and define a transformation route that uses the CollectNikeITPersonas component:

