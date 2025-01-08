from src.games.base_game import BaseGame
from src.utils.mapping import module_mapping


class FindGame(BaseGame):
    example = {
        "question": "تُعد قارة أكبر قارات العالم من حيث المساحة والسكان.",
        "answer": "آسيا",
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
        self.level = level
        self.module = module

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
        self.prompt += f"""Given the following question: {self.example['question']}?, an example answer in JSON format is: {self.example['answer']}.
        
        """

    def prepare_body(self):
        
        print(self.module)
        self.prompt += f"""You are asked to do the same for a question of your choice in {module_mapping[self.module]}. 
        
        """

    def prepare_outro(self):
        self.prompt += """ Please note the following: return ONLY a JSON as output with no addition."""
