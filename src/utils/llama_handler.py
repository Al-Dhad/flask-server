import replicate
import os

from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from src.utils.config.get_hgf_pass import getpass

from src.utils.config.llm_config import llm_config, llama_config
from src.utils.config.output_formatter import repair_json

HUGGINGFACEHUB_API_TOKEN = ""

os.environ['REPLICATE_API_TOKEN'] = ""


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


def ask_llm_replicate(question):
    input = {**llama_config, "prompt": question}

    output = replicate.run("meta/meta-llama-3-70b-instruct", input=input)

    output = "".join(output)

    return repair_json(output)


def llm_query_handler(prompt):
    game = ask_llm(prompt)

    game = repair_json(game)
    return {"game": game}
