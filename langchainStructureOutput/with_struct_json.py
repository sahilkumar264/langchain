from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Annotated , TypedDict , Optional , Literal


load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

#schema
json_schema = {
    "title": "Review",
    "type": "object",
    "description": "A movie review",
    "properties": {
        "summary": {
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "A brief summary of the movie"
        },
        "sentiment": {
            "type": "string",
            "description": "The overall sentiment of the review, e.g., positive, negative, neutral"
        }
    },
    "required": ["summary", "sentiment"]
}



structure_model = model.with_structure_output(json_schema)

result = structure_model.invoke("Write a review for the movie Inception") #give any review

print(type(result))