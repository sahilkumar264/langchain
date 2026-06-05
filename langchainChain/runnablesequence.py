from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch , RunnableLambda , RunnableSequence
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
    template =  "write a joke about {topic}",
    input_variables= ["topic"]
)

template2 = PromptTemplate(
    template = "Explain the joke - {text}",
    input_variables= ["joke"]
)

chain = RunnableSequence(template1 , model , parser , template2 , model , parser)

print(chain.invoke({'topic': 'AI'}))
