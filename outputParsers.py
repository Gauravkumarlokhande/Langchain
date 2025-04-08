from intro import groq_api_key,model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate


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
print("OUTPUT:-----",response)

