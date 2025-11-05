from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import Model

creds = Credentials(
    api_key="TON_API_KEY",
    url="https://eu-de.ml.cloud.ibm.com"  # ou autre région affichée
)

model = Model(
    model_id="mistralai/mixtral-8x7b-instruct",   # choisi dans Model Garden
    credentials=creds,
    project_id="TON_PROJECT_ID"                    # affiché dans watsonx.ai
)

result = model.generate_text(
    prompt="Explique la différence entre embeddings et LLM en 5 lignes.",
    max_new_tokens=120,
    temperature=0.7
)

print(result)
