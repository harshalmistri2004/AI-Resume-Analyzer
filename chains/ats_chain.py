from langchain_core.prompts import ChatPromptTamplate
from pydantic import BaseModel
from typing import List

from prompt.prompt_reader import get_ats_prompt

class ATSResponse(BaseModel):
    ats_score : int
    strengths : List[str]
    weaknesses : list[str]
    missing_keywords : list[str]
    improvements : list[str]
    suumary : str

def create_context(resume_text):
    return f"""
    System Prompt : {get_ats_prompt()}
    Resume : {resume_text}
    """

def analyze_resume(resume_text : str, llm):
    context = create_context(resume_text)
    prompt = ChatPromptTamplate.from_messages([("human", context)])
    print(prompt)

