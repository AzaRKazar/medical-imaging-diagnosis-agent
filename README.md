# Medical Imaging Diagnosis Agent

A Medical Imaging Diagnosis Agent built on Streamlit + Ollama (LLaVA) that provides AI-assisted analysis of medical images such as X-rays, MRIs, CT scans, and ultrasounds. The agent acts as a virtual radiology assistant to analyze images, highlight findings, suggest possible diagnoses, and provide patient-friendly explanations --- all while running fully local for privacy and cost efficiency.

**Output (AI-generated Report):**

<p align="center">
  <img src="sample_outputs/output_example.png" alt="AI Diagnostic Output" width="600"/>
</p>

## Features

- **Comprehensive Image Analysis**

  - Image Type Identification (X-ray, MRI, CT, Ultrasound)

  - Anatomical Region Detection

  - Key Findings and Observations

  - Potential Abnormalities Detection

  - Image Quality Assessment

  - Research and Reference (DuckDuckGo search)

- **DICOM Support (Experimental)**

  - Basic DICOM file parsing via pydicom

  - Metadata extraction and display

  - Window level/width adjustment for CT scans

## How to Run

### 1. Setup Environment

```bash

# Clone the repository

git clone https://github.com/<your-username>/medical_imaging_agent.git

cd medical_imaging_agent

# Create virtual environment

python -m venv .venv

# Activate (Windows)

.venv\Scripts\Activate

# Or activate (Mac/Linux)

source .venv/bin/activate

# Install dependencies

pip install -r requirements.txt

```

### 2. Install Ollama

Download Ollama from https://ollama.com/download

Pull a multimodal model:

```bash

ollama pull llava:7b

```

Start the Ollama server:

```bash

ollama serve

```

### 3. Run the Application

```bash

streamlit run app.py

```

Open in browser → http://localhost:8501

## Analysis Components

- **Image Type and Region**

  - Identifies imaging modality

  - Specifies anatomical region

- **Key Findings**

  - Systematic listing of observations

  - Detailed appearance descriptions

  - Abnormality highlighting

- **Diagnostic Assessment**

  - Primary and differential diagnoses

  - Confidence levels

  - Severity assessment

- **Patient-Friendly Explanations**

  - Simplified terminology

  - Clear analogies and definitions

  - Addresses common patient concerns

- **Research Context**

  - Fetches relevant recent literature

  - Links to treatment protocols

  - Highlights latest advances in imaging AI

## DICOM Support (Experimental)

The application includes basic DICOM support through the pydicom library:

```python

import pydicom

# Load DICOM file

ds = pydicom.dcmread("path/to/file.dcm")

# Access metadata

patient_name = ds.PatientName

modality = ds.Modality

study_date = ds.StudyDate

```

**Current DICOM Features:**

- Basic metadata extraction

- Image data extraction

- Window level/width adjustment for CT scans

- DICOM to standard image format conversion

**To enable DICOM support:**

```bash

pip install pydicom

```

## Notes

- Uses LLaVA via Ollama for multimodal analysis (image + text)

- Runs fully offline on your machine (no API costs)

- Recommended model: llava:7b (lighter, stable). llava:13b may require high-end hardware

- For educational and development purposes only

- Not a replacement for professional medical diagnosis

## Disclaimer

This tool is for educational and informational purposes only.

All analyses should be reviewed by qualified healthcare professionals.

⚠️ Do not make medical decisions based solely on this analysis.
