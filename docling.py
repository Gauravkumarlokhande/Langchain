from langchain_docling import DoclingLoader

FILE_PATH = "/root/langchain/NIPS-2017-attention-is-all-you-need-Paper.pdf"

loader = DoclingLoader(file_path=FILE_PATH)
docs = loader.load()
for d in docs[:3]:
    print(f"- {d.page_content=}")