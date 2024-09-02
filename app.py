import streamlit as st
import os 
import base64
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Initialize Streamlit app
st.set_page_config(page_title="Gemini_Decode")

# load all the environment variables
load_dotenv()  
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# UI elements
st.header("Gemini_Decode: Document Extraction")
text = "This effortlessly extracts vital information from diverse multilingual documents, transcending language barriers with precision and efficiency for enhanced productivity and decision-making."
styled_text = f"<span style='font-family:serif;'>{text}</span>" 
st.markdown(styled_text, unsafe_allow_html=True)

input = st.text_input("Input : ", key = "input")
uploaded_file = st.file_uploader("Choose an image of the document: ", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
submit = st.button("Submit")

# If submit button is clicked
if submit:
    response = get_response(input, image)
    st.subheader("Bot Response:")
    st.write(response)