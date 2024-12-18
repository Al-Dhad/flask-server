from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from utils.config.get_hgf_pass import getpass

from utils.config.llm_config import llm_config
from utils.config.output_formatter import repair_json

HUGGINGFACEHUB_API_TOKEN = "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"

def ask_llm(question):
    prompt = PromptTemplate.from_template(llm_config["template"])

    llm = HuggingFaceEndpoint(
        repo_id=llm_config["repo_id"],
        max_length=llm_config["max_length"],
        temperature=llm_config["temperature"],
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    )
    llm_chain = prompt | llm
    
    out = llm_chain.invoke({"question": question})

    print("answer ", out)
    return out

def llm_query_handler(prompt):
    print("prompt ", prompt)
    game = ask_llm(prompt)
    
    game = repair_json(game)
    return {'game':game}
