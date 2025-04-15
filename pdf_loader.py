# loading a pdf file
import asyncio
file_path=r"/root/langchain/form 12BB.pdf"
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path)
async def main():
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
    print(pages[0].page_content[:100])
    print(pages[0].metadata) 

asyncio.run(main())

# this can read pdf files only and not images in pdf or scanned pdf files 