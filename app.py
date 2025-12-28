import streamlit as st
from PIL import Image
from gemini_util import gemini_response
from pdf_utils import generate_nutrition_pdf

# Page config
st.set_page_config(
    page_title="Nutritionist AI",
    page_icon="🥗",
    layout="wide"
)

st.title("🥗 Nutritionist AI")
st.write("Upload a food image to analyze its nutritional value.")

# File uploader
uploaded_file = st.file_uploader(
    "Upload a food image",
    type=["jpg", "jpeg", "png"]
)

# Prompt for Gemini
PROMPT = """
You are a professional nutritionist.

Analyze the uploaded food image and return ONLY in the following format:

Dish Name: <dish name>

Item | Calories | Protein | Carbohydrates | Fats | Fiber
"""

# When image is uploaded
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Meal", use_column_width=True)

    if st.button("Analyze Meal"):
        with st.spinner("Analyzing meal..."):
            image_data = [{
                "mime_type": uploaded_file.type,
                "data": uploaded_file.getvalue()
            }]

            response = gemini_response(PROMPT, image_data)

        st.success("Analysis Complete!")

        st.subheader("📊 Nutrition Analysis")
        st.text(response)

        # Generate PDF
        pdf = generate_nutrition_pdf(response)

        st.download_button(
            label="📄 Download Nutrition PDF",
            data=pdf,
            file_name="nutrition_report.pdf",
            mime="application/pdf"
        )
