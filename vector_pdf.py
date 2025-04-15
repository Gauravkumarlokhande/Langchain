
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.embeddings import GroqEmbeddings

# groq_embeddings = GroqEmbeddings(api_key=os.environ["GROQ_API_KEY"])

# vector_store = InMemoryVectorStore.from_documents(pages, OpenAIEmbeddings())
# docs = vector_store.similarity_search("What is LayoutParser?", k=2)
# for doc in docs:
#     print(f'Page {doc.metadata["page"]}: {doc.page_content[:300]}\n')