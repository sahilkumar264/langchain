from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from dotenv import load_dotenv

load_dotenv()



llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)


class Person(BaseModel):
    name: str = Field(description="name of the person")
    age: int = Field(description="age of the person")
    city: str = Field(description="city of the person")

parser = PydanticOutputParser(pydantic_object = Person)

template = PromptTemplate(
    template = 'write a fictional name ,age,city of fictional {place} person \n {format_instructions}',
    input_variables = ['place', 'format_instructions'],
    partial_variables = {'format_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({'place': 'Indian'})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser
final_result = chain.invoke({'place' : 'chinese'})
print(final_result)
print(type(final_result))