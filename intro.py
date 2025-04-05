

import getpass
import os

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = "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"

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

# Example conversation
examples = [
    {"input": "What's 2 + 2?", "output": "The answer is 4."},
    {"input": "Who discovered gravity?", "output": "Isaac Newton discovered gravity."},
]

# Initialize the model
model = init_chat_model("llama3-8b-8192", model_provider="groq")

# Format examples into the template
formatted_examples = [example_prompt.format(**ex) for ex in examples]

# New question to ask
new_input = {"input": "Who is the founder of Microsoft?"}

# Create a chain and invoke
chain = example_prompt | model
response = chain.invoke(new_input)

# Print the response
print(response.content)
# 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