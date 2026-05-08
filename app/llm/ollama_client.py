import ollama
import yaml

with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    
MODEL_NAME = config["model"]

def generate_response(messages):
    response = ollama.chat(
    MODEL_NAME,
    messages=messages,
    stream=True,
    options={
        "temperature": config["generation"]["temperature"],
        "top_p": config["generation"]["top_p"],
        "max_tokens": config["generation"]["max_tokens"]
    },
    )
    
    return response
