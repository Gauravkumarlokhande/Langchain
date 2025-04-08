from langchain_groq import ChatGroq
from intro import groq_api_key,model
import asyncio

# this is an example of sync streaming
# for chunk in model.stream("Write me a 1 verse song about goldfish on the moon"):
#     print(chunk.content, flush=True)


# this is an example of async streaming
async def main():
    async for chunk in model.astream("Write me a 1 verse song about goldfish on the moon"):
        print(chunk.content)

# Run the async function
asyncio.run(main())

'''
 stream() (Synchronous Streaming):

What it does: Processes and yields output chunks synchronously as they are produced.​

When to use: In standard (non-asynchronous) Python environments where tasks are executed sequentially.

astream() (Asynchronous Streaming):

What it does: Processes and yields output chunks asynchronously, allowing other tasks to run concurrently.​

When to use: In asynchronous Python environments where you want non-blocking operations.

astream_events() (Asynchronous Event Streaming):

What it does: Streams detailed events, including intermediate steps and custom events, providing deeper insights into the processing pipeline.​


When to use: When you need access to intermediate outputs or detailed event data during the execution of a chain or model.
'''