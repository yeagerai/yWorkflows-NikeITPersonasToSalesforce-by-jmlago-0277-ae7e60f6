
from typing import Dict, List, Any
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class ExtractNameAndEmailInputDict(BaseModel):
    persona_list: List[Dict[str, Any]]


class ExtractNameAndEmailOutputDict(BaseModel):
    name_email_list: List[Dict[str, str]]


class ExtractNameAndEmail(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: ExtractNameAndEmailInputDict
    ) -> ExtractNameAndEmailOutputDict:
        result = []

        for persona in args.persona_list:
            if 'name' in persona and 'email' in persona:
                result.append({
                    'name': persona['name'],
                    'email': persona['email']
                })

        output = ExtractNameAndEmailOutputDict(name_email_list=result)
        return output


extract_name_and_email_app = FastAPI()


@extract_name_and_email_app.post("/transform/")
async def transform(
    args: ExtractNameAndEmailInputDict,
) -> ExtractNameAndEmailOutputDict:
    extract_name_and_email = ExtractNameAndEmail()
    return extract_name_and_email.transform(args)
