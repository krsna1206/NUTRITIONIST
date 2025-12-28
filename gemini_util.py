import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_response(prompt, image):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content([prompt, image[0]])
    return response.text
