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
    template = "Generate a tweet about {topic}",
    input_variables= ["topic"]
)


template2 = PromptTemplate(
    template = "Generate a linldn post text for topic {topic}",
    input_variables=["topic"]
)

parallel_chain = RunnableParallel({
    "tweet" : RunnableSequence(template1 , model , parser),
    "linkldn" : RunnableSequence(template2 , model , parser)
})

result = parallel_chain.invoke({'topic' : "data entry"})

print(result['tweet'])
print(result['linkldn'])