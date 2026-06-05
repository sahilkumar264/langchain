from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

#prompt

template1 = PromptTemplate(
    template = "Give me detail summary of this topic {topic}",
    input_variables= ["topic"]
)

template2 = PromptTemplate(
    template = "Genrate 5 pointer summary from following text {text}",
    input_variables= ["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic" : "Uttrakhand"})

print(result)

chain.get_graph().print_ascii()