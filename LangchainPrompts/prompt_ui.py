from langchain_google_genai import GoogleGenerativeAI
import streamlit as st 
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
load_dotenv()
model = GoogleGenerativeAI(model="gemini-2.5-flash")
st.header("Paper Summarizer")
paper_input = st.selectbox("Select the reseach paper",["Select.....", "Attention is all you need", "Diffusion models beat gan on image synthesis", "Learning Transferable Visual Models From Natural Language Supervision","Distilling the Knowledge in a Neural Network","CvT:Introducing Convolutions to Vision Transformers","BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation","End-to-End Object Detection with Transformers","Going deeper with convolutions"])
style_input = st.selectbox("Select explanation style",["Beginner Friendly","Code Oriented","Mathematical","Technical"])
length_input = st.selectbox("Select Explanation Length",["Short(1-2 paragraphs)","Medium(3-5 paragraphs)","Long(Detailed explanation)"])
#Design the prompt template
template = load_prompt('template.json')

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result)

