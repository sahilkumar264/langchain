from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)
#1st prompt -> detail prompt
template1 = PromptTemplate(
    template = 'Write a detail on the following text ./n {text}',
    input_variables = ['text']
)

#2ndprompt -> summary

template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text ./n {text}',
    input_variables = ['text']
)

prompt1 = template1.invoke({'text': 'Artificial Intelligence'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result2 = model.invoke(prompt2)

print(result.content)
print()
print(result2.content)

