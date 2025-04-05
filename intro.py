

import getpass
import os

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = "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"
import langchain
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("placeholder", "{msgs}") # <-- This is the changed part
])


# Initialize the model
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Create a chain and invoke
chain = prompt_template | model
response = chain.invoke("hello")

# Print the response
print(response.content)
# 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