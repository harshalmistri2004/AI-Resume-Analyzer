import os

PROMPT_DIR = os.path.dirname(os.path.abspath("__file__"))

def get_ats_prompt():
    with open(os.path.join("PROMPT_DIR", "ats_prompt.md")) as file:
        return file.read()