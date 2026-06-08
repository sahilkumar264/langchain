from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)
parser = StrOutputParser()

template1 = PromptTemplate(
    template = 'write a summary of given text {text}',
    input_variables= ['text']
)

loader = TextLoader('cricket.txt' , encoding = 'utf-8')
docs = loader.load()
# print(docs[0])

chain = template1 | model | parser
result = chain.invoke({'text' : docs[0]})

print(result)