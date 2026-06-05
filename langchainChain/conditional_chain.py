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

class Feedback(BaseModel):
    sentiment: Literal['positive' , 'negative'] = Field(description="give me sentiment of the feedback")


parser2 = PydanticOutputParser(pydantic_object = Feedback)
template1 = PromptTemplate(
    template = "classify the sentiment of the follwing feedback into postive or negative {feedback} {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = template1 | model | parser2

# result = classifier_chain.invoke({'feedback':'this is terrible smartphone'})

# print(result.sentiment)

# branch_chain = RunnableBranch(
#     (condition1 , chain1),
#     (condition2 , chain2)
#     default chain
# )

template2 = PromptTemplate(
    template = "Write an appropriate response to this negative feedback {feedback}",
    input_variables=["feedback"]
)

template3 = PromptTemplate(
    template = "Write an appropriate response to this postive feedback {feedback}",
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive' , template3 | model | parser),
    (lambda x : x.sentiment == 'negative' , template2 | model | parser),
    RunnableLambda(lambda x : "could not find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({"feedback" : "this is a terrible phone"})

print(result)

chain.get_graph().print_ascii()