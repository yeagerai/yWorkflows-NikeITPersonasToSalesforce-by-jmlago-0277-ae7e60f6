
import os
from typing import List, Dict, Any

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent
from salesforce_api import SalesforceAPI  # Assuming there's a salesforce_api.py file handling the API integration


class SendToSalesforceInputDict(BaseModel):
    name_email_list: List[Dict[str, str]]
    salesforce_credentials: Dict[str, Any]


class SendToSalesforceOutputDict(BaseModel):
    successful_imports: int
    total_imported: int


class SendToSalesforce(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: SendToSalesforceInputDict
    ) -> SendToSalesforceOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        # Authenticate with Salesforce API using the provided salesforce_credentials
        salesforce_api = SalesforceAPI(args.salesforce_credentials)

        successful_imports = 0
        total_imported = 0

        # Iterate through the name_email_list, sending each name and email to Salesforce
        for entry in args.name_email_list:
            result = salesforce_api.send_name_email(entry)
            total_imported += 1

            if result:
                successful_imports += 1

        out = SendToSalesforceOutputDict(
            successful_imports=successful_imports,
            total_imported=total_imported
        )

        return out


load_dotenv()
send_to_salesforce_app = FastAPI()


@send_to_salesforce_app.post("/transform/")
async def transform(
    args: SendToSalesforceInputDict,
) -> SendToSalesforceOutputDict:
    send_to_salesforce = SendToSalesforce()
    return send_to_salesforce.transform(args)

