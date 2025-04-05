
import os
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv




prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful assistant"),
    ("placeholder", "{msgs}") 
])


load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

# Initialize the model
model = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="llama3-8b-8192")

# Create a chain and invoke
chain = prompt_template | model
input_data = {"msgs": "Your message or conversation history here"}

# Invoke the chain with the input data
response = chain.invoke({"msgs": [HumanMessage(content="hi!")]})
print(response.content)