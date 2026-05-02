import streamlit as st
from preprocess import preprocess_pipeline

# Page config
st.set_page_config(
    page_title="Text Preprocessing Tool",
    page_icon="🧹",
    layout="centered"
)

st.title("🧹 NLP Text Preprocessing Tool")
st.write("Convert raw text into clean, machine-readable text")

# User input
input_text = st.text_area(
    "Enter Raw Text Below:",
    height=150,
    placeholder="Type or paste your text here..."
)

# Button
if st.button("Preprocess Text"):
    if input_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        result = preprocess_pipeline(input_text)

        st.subheader("✅ Cleaned Text")
        st.write(result["cleaned_text"])

        st.subheader("🔹 Tokens")
        st.write(result["tokens"])

        st.subheader("🚫 Stopwords Removed")
        st.write(result["tokens_no_stopwords"])

        st.subheader("📘 Lemmatized Tokens")
        st.write(result["lemmatized_tokens"])
