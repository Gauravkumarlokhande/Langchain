# loading web pages
from langchain_huggingface import HuggingFaceEmbeddings
import bs4
from langchain_community.document_loaders import WebBaseLoader
import os
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/root/langchain/NIPS-2017-attention-is-all-you-need-Paper.pdf")
pages = []
for page in loader.load():
    pages.append(page)
# print(pages)

hf_token = os.environ.get("HUGGINGFACEHUB_API_TOKEN")

page_url = "https://python.langchain.com/docs/how_to/chatbots_memory/"

loader = WebBaseLoader(web_paths=[page_url])
docs = []
for doc in loader.load():
    docs.append(doc)

assert len(docs) == 1
doc = docs[0]
# print(f"{doc.metadata}\n")
# print(doc.page_content[:500].strip())

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vector_store = InMemoryVectorStore.from_documents(pages, embeddings)
docs = vector_store.similarity_search("What are Encoder and Decoder Stacks?", k=2)
for doc in docs:
    print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')

