from games.base_game import BaseGame
import requests


class FillGame(BaseGame):
    def __init__(self):
        super(BaseGame, self).__init__()

        self.prompt = ""

        self.seed_pieces = []

    def _BaseGame__build_prompt(self, level, module):
        self._BaseGame__load_seed_pieces(level, module)

        self._BaseGame__prepare_prompt_salt()
        self._BaseGame__prepare_prompt_task()
        self._BaseGame__prepare_prompt_task_notices()
        self._BaseGame__prepare_prompt_pepper()

    def _BaseGame__load_seed_pieces(self, level, module):
        response = requests.get(
            f"http://localhost:3000/api/v1/words/fill-game?level={level}&module={module}"
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
        self.prompt += f"Please note the following: you cannot use the same word twice. You shall return a SINGLE and MEANINGFUL sentence and it should be in ARABIC. And You shall return the JSON ONLY "

    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {sentence: the resulting sentence}) AND with no extra information or explanation (only the JSON). "
