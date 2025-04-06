from langchain_core.globals import set_llm_cache
from langchain_groq import ChatGroq
from intro import groq_api_key,model
from langchain_core.caches import InMemoryCache

# Inmemory cache is a caching mechanism that uses the RAM allocated to our application in which we are running our llm model.
# here this means that our local systems RAM is being used.

# //// uncoment when using inmemory cache ////

# set_llm_cache(InMemoryCache())
# response=model.invoke("tell me a joke")
# print(response.content)

#if we wish to add that cache into some databse instead of storing it into the local system, we can use langchain's sqlitecache to store the cache into some database.

from langchain_community.cache import SQLiteCache

set_llm_cache(SQLiteCache(database_path=".langchain.db"))
response=model.invoke("tell me a horror story")
print(response.content)