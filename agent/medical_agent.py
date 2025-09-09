from agno.agent import Agent
from agno.models.ollama import Ollama

def get_medical_agent(model: str = "llava:latest"):
    """
    Initializes the Medical Imaging Diagnosis Agent with local LLM.
    Default is llava:13b (multimodal) for medical image analysis.
    Ollama models do not support tool-calling, so no tools are attached here.
    """
    return Agent(
        model=Ollama(id=model),
        markdown=True
    )
