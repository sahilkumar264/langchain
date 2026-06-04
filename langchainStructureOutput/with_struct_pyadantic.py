from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Annotated , TypedDict , Optional , Literal

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

#schema
class Review(BaseModel):
    summary: list[str] = Field(description="A brief summary of the movie")
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="The overall sentiment of the review, e.g., positive, negative, neutral")

    # summary: Annotated[str , "A brief summary of the movie"] # annotated means we can add description to the field in the schema
    # sentiment: Annotated[str , "The overall sentiment of the review, e.g., positive, negative, neutral"]

structure_model = model.with_structure_output(Review)

result = structure_model.invoke("Write a review for the movie Inception") #give any review

print(type(result))