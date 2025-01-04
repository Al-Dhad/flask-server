llm_config = {
    "template": """Question: {question}

    Answer: As an Arab Language teacher. I am going to reply to your question, so here is my response.""",
    "repo_id": "mistralai/Mistral-7B-Instruct-v0.2",
    "max_length": 50,
    "temperature": 0.5,
}

llama_config = {
    "max_new_tokens": 512,
    "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "system_prompt": "You are a helpful arabic teacher, that knows a lot about arabic vocabulary, and can make quizes for kids.",
}
