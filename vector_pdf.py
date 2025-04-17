# loading web pages

import bs4
from langchain_community.document_loaders import WebBaseLoader

page_url = "https://python.langchain.com/docs/how_to/chatbots_memory/"

loader = WebBaseLoader(web_paths=[page_url])
docs = []
for doc in loader.load():
    docs.append(doc)

assert len(docs) == 1
doc = docs[0]
print(f"{doc.metadata}\n")
print(doc.page_content[:500].strip())
# groq_embeddings = GroqEmbeddings(api_key=os.environ["GROQ_API_KEY"])

# vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings())
# docs = vector_store.similarity_search("What is LayoutParser?", k=2)
# for doc in docs:
#     print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')