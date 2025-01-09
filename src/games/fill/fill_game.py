from src.games.base_game import BaseGame
from src.utils.config.express_server import EXPRESS_SERVER_URL
from src.utils.retrieve_passages import fetch_retrieved_passages

import requests


class FillGame(BaseGame):
    example = {
        "1": {
            "words": ["تذكرنا", "بالرحلة", "التذكارات"],
            "sentence": "لقد جمعنا التذكارات بالرحلة عندما تذكرنا الأيام السعيدة",
        },
        "2": {
            "words": ["الاستقلال", "ثورة", "الجزائر"],
            "sentence": "حققت الجزائر الاستقلال بعد ثورة عظيمة ضد الاستعمار.",
        },
        "4": {
            "words": ["الخلايا", "الحيوانات", "النباتات"],
            "sentence": "تتكون أجسام الحيوانات والنباتات من الخلايا التي تعد الوحدة الأساسية للحياة.",
        },
        "5": {
            "words": ["الصحراء", "الجزائر", "الكبرى"],
            "sentence": "تعد الصحراء الكبرى في الجزائر من أكبر الصحارى في العالم.",
        },
        "6": {
            "words": ["الإنترنت", "الحاسوب", "التواصل"],
            "sentence": "يُستخدم الإنترنت عبر الحاسوب لتسهيل التواصل بين الناس حول العالم.",
        },
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
        self.module = module
        self.level = level

        response = requests.get(
            f"{EXPRESS_SERVER_URL}/api/v1/words/fill-game?level={level}&module={module}"
        )

        if response.status_code == 200:
            self.seed_pieces = response.json().get("data", [])
        else:
            self.seed_pieces = []

        if self.module in self.example.keys():
            self.retrieved_passages = fetch_retrieved_passages(self.level, self.module)

            self.prompt += """Given the following passages: 
            
            """
            for passage in self.retrieved_passages:
                self.prompt += f""" {passage}.
                
                """

    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {', '.join(self.seed_pieces)}. "

    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to generate a sentence that uses those words: {', '.join(self.seed_pieces)}. "

    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += "Please note the following: you cannot use the same word twice. You shall return only ONE and MEANINGFUL sentence and it should be in ARABIC. And You shall return the JSON ONLY "

    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {sentence: the resulting sentence}) AND with no extra information or explanation (only the JSON). "

    def build_prompt_in_few_shots(self):
        self.perpare_intro()
        self.prepare_body()
        self.prepare_outro()

    def perpare_intro(self):
        self.prompt += f"""Given the following arabic words: {', '.join(self.example[self.module]['words'])}, an example output is: {{words: [{', '.join(self.example[self.module]['words'])}], sentence: [{self.example[self.module]['sentence']}] }} 
        
        """

    def prepare_body(self):
        self.prompt += f"""You are asked to do the same for the following words: {', '.join(self.seed_pieces)}. 
        
        """

    def prepare_outro(self):
        self.prompt += """ Please note the following: return ONLY a JSON as output with no addition."""
