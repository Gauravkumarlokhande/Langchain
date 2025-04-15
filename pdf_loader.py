# loading a pdf file
import asyncio
file_path=r"/root/langchain/form 12BB.pdf"
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path)
# print(loader.load())
async def main():
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
        print(pages) 

asyncio.run(main())


# this can read pdf files only and not images in pdf or scanned pdf files 