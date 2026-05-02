from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# UI Title
st.title("🤖 AI Explainer (Mistral + LangChain)")

# Input box
topic = st.text_input("Enter a topic:", "quantum computing")

# Button
if st.button("Explain"):

    # Prompt
    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in simple words"
    )

    # Model
    model = ChatMistralAI(model="mistral-small")

    # Parser
    parser = StrOutputParser()

    # Chain
    chain = prompt | model | parser

    # Run
    result = chain.invoke({"topic": topic})

    # Output
    st.write("### 📖 Explanation:")
    st.write(result)












