from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from langchain.chains import LLMChains


# prompt template

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# model 
model =ChatMistralAI(model="mistral-small-2506")

# output parser
parser=StrOutputParser()


chain = prompt | model | parser


result =chain.invoke({"topic": "quantum computing"})
print(result)














import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title("🧠 AI Code Analyzer")

code_input = st.text_area("Paste your code here:")

if st.button("Analyze Code"):

    prompt = ChatPromptTemplate.from_template("""
    You are an expert DSA tutor.

    Analyze this code:

    {code}

    Provide:
    1. Explanation
    2. Time Complexity
    3. Space Complexity
    4. Algorithm Used
    5. Alternative Approaches
    6. Best Approach
    """)

    model = ChatMistralAI(model="mistral-small")
    parser = StrOutputParser()

    chain = prompt | model | parser

    result = chain.invoke({"code": code_input})

    st.write(result)