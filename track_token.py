from langchain_community.callbacks import get_openai_callback
from intro import groq_api_key,model
from langchain_groq import ChatGroq


with get_openai_callback() as cb:
    result = model.invoke("Tell me a joke")
    print(result)
    print("---")
print()

print(f"Total Tokens: {cb.total_tokens}")
print(f"Prompt Tokens: {cb.prompt_tokens}")
print(f"Completion Tokens: {cb.completion_tokens}")
print(f"Total Cost (USD): ${cb.total_cost}")