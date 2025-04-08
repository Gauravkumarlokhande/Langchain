from intro import groq_api_key,model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Joke(BaseModel):
    setup: str = Field(description="The setup or question part of the joke")
    punchline: str = Field(description="The punchline or answer part of the joke")

# string output parser
chain= model | StrOutputParser()
respon=chain.invoke("Hi My name is chunkey pandey")
# print("OUTPUT: ------",respon)


prompt = PromptTemplate(
    template="Provide a JSON object with an 'answer' key that addresses the following question: {question}",
    input_variables=["question"]
)


chain_2=prompt |model | JsonOutputParser()
response=chain_2.invoke({"question":"Hi My name is chunkey pandey"})
# print("OUTPUT:-----",response)


parser3 = PydanticOutputParser(pydantic_object=Joke)
prompt3 = PromptTemplate(
    template="Tell me a joke.\n{format_instructions}\n",
    input_variables=[],
    partial_variables={"format_instructions": parser3.get_format_instructions()},
)
chain_3=prompt3 | model | parser3
res=chain_3.invoke({})
print("OUTPUT:-----",res)
