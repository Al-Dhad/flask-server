from src.games.base_game import BaseGame
from src.utils.config.express_server import EXPRESS_SERVER_URL

import requests


class FillGame(BaseGame):
    example = {
        "words": ["تذكرنا", "بالرحلة", "التذكارات"],
        "sentence": "لقد جمعنا التذكارات بالرحلة عندما تذكرنا الأيام السعيدة",
    }

    def __init__(self):
        super(BaseGame, self).__init__()

        self.prompt = ""

        self.seed_pieces = []

    def _BaseGame__build_prompt(self, level, module):
        self._BaseGame__load_seed_pieces(level, module)

        self.build_prompt_in_few_shots()

    def build_prompt_in_zero_shot(self):
        self._BaseGame__prepare_prompt_salt()
        self._BaseGame__prepare_prompt_task()
        self._BaseGame__prepare_prompt_task_notices()
        self._BaseGame__prepare_prompt_pepper()

    def _BaseGame__load_seed_pieces(self, level, module):
        response = requests.get(
            f"{EXPRESS_SERVER_URL}/api/v1/words/fill-game?level={level}&module={module}"
        )

        print("response", response.json().get("data", []))
        if response.status_code == 200:
            self.seed_pieces = response.json().get("data", [])
        else:
            self.seed_pieces = []

    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {', '.join(self.seed_pieces)}. "

    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to generate a sentence that uses those words: {', '.join(self.seed_pieces)}. "

    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot use the same word twice. You shall return only ONE and MEANINGFUL sentence and it should be in ARABIC. And You shall return the JSON ONLY "

    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {sentence: the resulting sentence}) AND with no extra information or explanation (only the JSON). "

    def build_prompt_in_few_shots(self):
        self.perpare_intro()
        self.prepare_body()
        self.prepare_outro()

    def perpare_intro(self):
        self.prompt += f"""Given the following arabic words: {', '.join(self.example['words'])}, an example sentence is: {{words: [{', '.join(self.example['words'])}], sentence: [{self.example['sentence']}] }} 
        
        """

    def prepare_body(self):
        self.prompt += f"""You are asked to do the same for the following words: {', '.join(self.seed_pieces)}. 
        
        """

    def prepare_outro(self):
        self.prompt += f""" Please note the following: return ONLY a JSON as output with no addition."""
