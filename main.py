from langchain_aws import BedrockLLM
from langchain_classic.chains import LLMChain
from langchain_classic.prompts import PromptTemplate
import boto3, os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
region_name = os.getenv("region_name")

# Bedrock client
bedrock = boto3.client(
    service_name = "bedrock-runtime",
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

model_id = "meta.llama3-8b-instruct-v1:0"

llm = BedrockLLM    (
    model_id = model_id,
    client = bedrock,
    model_kwargs={"temperature":0.9}
)

def my_chatbot(language, user_text):
    prompt = PromptTemplate(
        input_variables = ["language","user_text"],
        template="""
You are a helpful chatbot.
Answer the following question in {language}.

Question:
{user_text}
"""
)
    chain = prompt | llm
    response=chain.invoke({'language':language,'user_text':user_text})
    return response

st.title('Bedrock chat Demo')

language = st.sidebar.selectbox("Language", ["english","spanish","hindi"])

if language:
    user_text = st.sidebar.text_area(label="What is your question?",max_chars=100)

if user_text:
    response = my_chatbot(language,user_text)
    st.write(response)