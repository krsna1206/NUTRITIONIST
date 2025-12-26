import streamlit as st
from PIL import Image
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_response(prompt,image):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([prompt, image[0]])
    return response.text

def input_image_Setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise ValueError("No image uploaded")
    
st.title("Nutritionist AI")
st.set_page_config(page_title="Nutritionist AI", page_icon=":apple:", layout="wide")
uploaded_File = st.file_uploader("Upload an image of your meal", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_File is not None:
    image = Image.open(uploaded_File)
    st.image(image, caption='Uploaded Image', use_column_width=True)

submit = st.button("TELL ME ABOUT MY MEAL")

input_prompt = """You are a expert nutritionist. Anlayze the iamge of the meal and provide a detailed" \
"information about the meal. Mention the name of the dish, its nuttritional value, health benefits." \
"" \
"give the nutrional value in a table format. like:" \
"ITEMS    |   AMOUNT_of_calories  |  amount_of_protien " \
"item1_name        200g                    12g" \
"item2_name         150g                    9g" \
"also provide the whether the food is healthy and best alternative of that food" \
"mention the percentage split of the ratio of carbihydrates,fats,fibers,sugar any additional diet information""" 

if submit:
    
    image_data = input_image_Setup(uploaded_File)
    response = gemini_response(input_prompt,image_data)
    st.subheader("AI Response")
    st.write(response)