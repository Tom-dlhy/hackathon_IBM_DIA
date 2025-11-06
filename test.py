from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY")
URL=os.getenv("URL")
PROJECT_ID=os.getenv("PROJECT_ID")

print("IBM_API_KEY:", IBM_API_KEY)
print("URL:", URL)
print("PROJECT_ID:", PROJECT_ID)

creds = Credentials(
    api_key=IBM_API_KEY, 
    url=URL 
)

client = APIClient(creds, project_id=PROJECT_ID)

# To display example params enter
GenParams().get_example_values()

generate_params = {
    GenParams.MAX_NEW_TOKENS: 25
}

model_inference = ModelInference(
    model_id='mistralai/mistral-medium-2505',
    params=generate_params,
    credentials=creds,
    project_id=PROJECT_ID
)   

async def test_inference():
    response = await model_inference.agenerate(
        prompt="Write a short poem about the sea."
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(test_inference())