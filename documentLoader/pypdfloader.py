from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)
parser = StrOutputParser()
#  loader = PyPDFLoader('given.pdf')  #here only one pdf load
# docs = loader.load()
# print(docs[0].page_content)



#here multiple pdf load from a book named directory
loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls= PyPDFLoader
)

# docs = loader.load()
docs = loader.lazy_load()

print(docs[0].page_content)