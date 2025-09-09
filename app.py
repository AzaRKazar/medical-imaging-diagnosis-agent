import streamlit as st
from PIL import Image as PILImage
from agent.medical_agent import get_medical_agent
from agent.prompts import medical_prompt
from agno.media import Image as AgnoImage
import os

st.set_page_config(page_title="Medical Imaging Diagnosis Agent 🏥", layout="wide")

st.sidebar.title("ℹ️ Configuration")
model_choice = st.sidebar.selectbox(
    "Choose Local Model",
    ["llama3.1:8b", "mistral:7b-instruct", "llava:latest"]  # llava is good for multimodal
)
st.sidebar.info("Runs on Ollama (http://localhost:11434). Make sure the model is pulled.")

agent = get_medical_agent(model_choice)

st.title("🏥 Medical Imaging Diagnosis Agent")
st.write("Upload a medical image for AI-powered analysis (educational use only)")

uploaded_file = st.file_uploader(
    "Upload Medical Image",
    type=["jpg", "jpeg", "png", "dicom"]
)

if uploaded_file:
    image = PILImage.open(uploaded_file)
    st.image(image, caption="Uploaded Medical Image", use_container_width=True)

    if st.button("🔍 Analyze Image"):
        with st.spinner("Analyzing image..."):
            temp_path = "temp_uploaded.png"
            image.save(temp_path)

            agno_image = AgnoImage(filepath=temp_path)
            response = agent.run(medical_prompt, images=[agno_image])

            st.markdown("### 📋 Analysis Results")
            st.markdown("---")
            st.markdown(response.content)
            st.caption("⚠️ Disclaimer: This analysis is AI-generated. Always consult a medical professional.")
