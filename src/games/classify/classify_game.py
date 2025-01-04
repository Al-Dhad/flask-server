
from games.base_game import BaseGame

class ClassifyGame(BaseGame):

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
        # normally, we would load those from the DB
        self.seed_pieces =  ["السَّنَة", "الشَّهْر", "المُسْتَقْبَل", "المُتْحَف", "المَغَارَة"]
        
        self.seed_classes = ["المَكَانُ", "الزَّمَانُ"]
            
    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {', '.join(self.seed_pieces)}. "
   
    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to classify them into the following set of classes: ${", ".join(self.seed_classes)}. "
    
    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot classify the same word in more than once class. And make sure to use both classes in your output. "        
        
    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {class_1: [list of words]} ) AND with no extra information or explanation (only the JSON). "
        
        