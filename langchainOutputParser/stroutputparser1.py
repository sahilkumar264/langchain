from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
#1st prompt -> detail prompt
template1 = PromptTemplate(
    template = 'Write a detail on the topic ./n {text}',
    input_variables = ['text']
)

#2ndprompt -> summary

template2 = PromptTemplate(
    template = 'Write a 5 line summary on the topic ./n {text}',
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'text': 'Artificial Intelligence'})

print(result)

