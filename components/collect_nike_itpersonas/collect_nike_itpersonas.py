
import os
from typing import Any, Dict, List

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class CollectNikeITPersonasInputDict(BaseModel):
    organization_name: str
    department_name: str


class CollectNikeITPersonasOutputDict(BaseModel):
    persona_list: List[Dict[str, Any]]


class CollectNikeITPersonas(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()
        with open(self.component_configuration_path(), "r", encoding="utf-8") as file:
            yaml_data = yaml.safe_load(file)

    def transform(
        self, args: CollectNikeITPersonasInputDict
    ) -> CollectNikeITPersonasOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Step 1: Check if input organization_name and department_name are valid
        organization_name = args.organization_name
        department_name = args.department_name
        
        # Step 2: Here, assume API/database access to query personas
        # For the given input organization_name and department_name, query the API/database
        # and store the returned personas in the variable persona_list.

        # Replace this with actual API/database operation
        persona_list = [
            {"name": "John Doe", "role": "IT Manager"},
            {"name": "Jane Smith", "role": "IT Analyst"},
        ]
        
        # Step 3: Return the persona_list
        out = CollectNikeITPersonasOutputDict(persona_list=persona_list)
        return out


load_dotenv()
collect_nike_it_personas_app = FastAPI()


@collect_nike_it_personas_app.post("/transform/")
async def transform(
    args: CollectNikeITPersonasInputDict,
) -> CollectNikeITPersonasOutputDict:
    collect_nike_it_personas = CollectNikeITPersonas()
    return collect_nike_it_personas.transform(args)
