from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from utils.config.get_hgf_pass import getpass

from utils.llm_utils import (
    description_prompt_builder_from_response,
    causes_prompt_builder_from_response,
    treatement_prompt_builder_from_response,
    parse_llm_response_to_dict,
    prompt_builder_for_diagnose,
    prompt_builder_for_tip,
    prompt_builder_for_tip_detail,
    parse_llm_tip,
    build_prompt_for_game
)

from utils.config.llm_config import llm_config
from utils.config.output_formatter import repair_json

HUGGINGFACEHUB_API_TOKEN = "<YOUR TOKEN>"

def get_tip_from_llm(game_id = 'order_sentence'):
    game = ask_llm(build_prompt_for_game(game_id))
    
    game = repair_json(game)
    return {'game_id': game_id, 'game':game}
