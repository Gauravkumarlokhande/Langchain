from langchain_text_splitters import RecursiveCharacterTextSplitter

with open("/root/langchain/doc.txt") as f:
    docs = f.read()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=10)
texts = text_splitter.split_text(docs)

print(texts[0])