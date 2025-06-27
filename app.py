import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Free AI Story Generator", page_icon="🧠")

st.title("AI Story Generator- Generate your own story")
st.markdown("Enter a story idea below and get a short story generated using GPT-2.")

prompt = st.text_input("Enter your story idea (e.g., A robot finds a lost puppy):")

if st.button("Generate Story"):
    if not prompt:
        st.warning("Please enter a prompt!")
    else:
        with st.spinner("Generating story..."):
            
            generator = pipeline("text-generation", model="gpt2")
            result = generator(prompt, max_length=200, num_return_sequences=1)[0]["generated_text"]

            
            st.success("Here's your story:")
            st.write(result)
