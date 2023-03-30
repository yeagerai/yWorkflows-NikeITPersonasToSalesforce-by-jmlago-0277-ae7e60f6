
import typing
from typing import Dict, Any
from dotenv import load_dotenv
from pydantic import BaseModel
from fastapi import FastAPI
from core.workflows.abstract_workflow import AbstractWorkflow


class NikeITPersonasToSalesforceIn(BaseModel):
    organization_name: str
    department_name: str
    salesforce_credentials: Dict[str, Any]


class NikeITPersonasToSalesforceOut(BaseModel):
    successful_imports: int
    total_imported: int


class NikeITPersonasToSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NikeITPersonasToSalesforceIn, callbacks: typing.Any
    ) -> NikeITPersonasToSalesforceOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        # Extract outputs from `results_dict` and create the final output
        successful_imports = results_dict["successful_imports"].output
        total_imported = results_dict["total_imported"].output
        out = NikeITPersonasToSalesforceOut(
            successful_imports=successful_imports, total_imported=total_imported
        )

        return out


load_dotenv()
nike_it_personas_to_salesforce_app = FastAPI()


@nike_it_personas_to_salesforce_app.post("/transform/")
async def transform(
    args: NikeITPersonasToSalesforceIn,
) -> NikeITPersonasToSalesforceOut:
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()
    return await nike_it_personas_to_salesforce.transform(args, callbacks=None)

