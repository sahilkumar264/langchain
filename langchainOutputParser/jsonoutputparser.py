from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()
parser = JsonOutputParser()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template = 'write a fictional name ,age,city of fictional charact\n {format_instructions}',
    input_variables = ['format_instructions'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser
result = chain.invoke({})

print(result)