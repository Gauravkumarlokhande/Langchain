from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = PyPDFLoader("/root/langchain/NIPS-2017-attention-is-all-you-need-Paper.pdf")
pages=loader.load()
content=pages[0].page_content
text_splitter = CharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=100,
    chunk_overlap=50
)
raw_documents = TextLoader('/root/langchain/doc.txt').load()

texts = text_splitter.create_documents(raw_documents[0].page_content)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

db = Chroma.from_documents(texts, embeddings)

query = "what is decoder"
docs = db.similarity_search(query)
print(docs)
print(docs[0].page_content)