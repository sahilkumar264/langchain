from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9);
st.header("Research Tool")

user_input = st.text_input("Enter promopt")
# if st.button("Submit"):
#     result = model.invoke(user_input)
#     st.write(result.content)

#template
template = PromptTemplate(
    template = "what is the capital of {country}?"
)

#fill the placeholder
prompt = template.invoke(country="France")

if st.button("Submit"):
    result = model.invoke(prompt)
    st.write(result.content)