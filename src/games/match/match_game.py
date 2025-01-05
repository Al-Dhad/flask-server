from src.games.base_game import BaseGame


class MatchGame(BaseGame):
    tags = {1: "synonym", 2: "opposite"}

    example = {
        "synonym": {"كذب": "افترى", "قال": "تحدث", "ذهب": "غادر"},
        "opposite": {"كذب": "صدق", "قال": "سكت", "ذهب": "رجع"},
    }

    def __init__(self, goal_tag=1):
        super(BaseGame, self).__init__()

        self.prompt = ""

        self.goal_tag = self.tags[goal_tag]
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
        # normally, we would load those from the DB
        self.seed_pieces = ["تهوى", "تنظيم", "الوفي", "نجح"]

    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {', '.join(self.seed_pieces)}. "

    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to generate a single {self.goal_tag} for each of those words. "

    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += (
            f"Please note the following: you cannot use the same word twice. "
        )

    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {the given word: the result} with each word in its object) AND with no extra information or explanation (only the JSON). "

    def build_prompt_in_few_shots(self):
        self.perpare_intro()
        self.prepare_body()
        self.prepare_outro()

    def perpare_intro(self):
        self.prompt += f"""Given the following words: {', '.join(list(self.example[self.goal_tag].keys()))} and their correct {self.goal_tag}s: {self.example[self.goal_tag]}
        
        """

    def prepare_body(self):
        self.prompt += f"""You are asked to do the same for the following words: {', '.join(self.seed_pieces)}. 
        
        """

    def prepare_outro(self):
        self.prompt += f""" Please note the following: return ONLY a JSON as output with no addition."""
