from src.games.base_game import BaseGame


class ClassifyGame(BaseGame):
    def __init__(self):
        super(BaseGame, self).__init__()

        self.prompt = ""

        self.seed_pieces = []

        self.example = {
            "classes": ["المَكَانُ", "الزَّمَانُ"],
            "words": ["السَّنَة", "الشَّهْر", "المُسْتَقْبَل", "المُتْحَف", "المَغَارَة"],
            "result": {
                "المَكَانُ": ["المُتْحَف", "المَغَارَة"],
                "الزَّمَانُ": ["السَّنَة", "المُسْتَقْبَل", "الشَّهْر"],
            },
        }

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
        self.seed_pieces = ["البرد", "الشمس", "الثلج", "البحر"]

        self.seed_classes = ["الصيف", "الشتاء"]

    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {', '.join(self.seed_pieces)}. "

    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to classify them into the following set of classes: ${', '.join(self.seed_classes)}. "

    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot classify the same word in more than once class. And make sure to use both classes in your output. "

    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {class_1: [list of words]} ) AND with no extra information or explanation (only the JSON). "

    def build_prompt_in_few_shots(self):
        self.perpare_intro()
        self.prepare_body()
        self.prepare_outro()

    def perpare_intro(self):
        self.prompt += f"""Given the following arabic words: {', '.join(self.example['words'])}, and those classes: {', '.join(self.example['classes'])}, an example classification is: {self.example['result']}
        
        """

    def prepare_body(self):
        self.prompt += f"""You are asked to do the same for the following words: {', '.join(self.seed_pieces)}, and those classes: {', '.join(self.seed_classes)}.
        
        """

    def prepare_outro(self):
        self.prompt += f""" Please note the following: return ONLY a JSON as specified with no addition. make sure to use ALL the words."""
