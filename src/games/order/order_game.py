
from src.games.base_game import BaseGame

class OrderGame(BaseGame):
    
    tags = {
        1: "words",
        2: "characters"
    }
    
    goal_tags = {
        1: "sentence",
        2: "word"
    }
    
    def __init__(self, type_=1):
        super(BaseGame, self).__init__()
        
        self.prompt = ""
        
        self.type = type_
        self.seed_pieces = []
        
        self.seed_tag = self.tags[self.type]
        self.goal_tag = self.goal_tags[self.type]
        
    def _BaseGame__build_prompt(self, level, module):
        self._BaseGame__load_seed_pieces(level, module)
        
        self._BaseGame__prepare_prompt_salt()
        self._BaseGame__prepare_prompt_task()
        self._BaseGame__prepare_prompt_task_notices()
        self._BaseGame__prepare_prompt_pepper()
    
    def _BaseGame__load_seed_pieces(self, level, module):
        # normally, we would load those from the DB
        if self.type == 1:
            self.seed_pieces =  ["قرأ", "بصمت", "الكتاب", "الأب"]
        else:
            self.seed_pieces =  ["ت", "ق", "ل", "ب", "م"]
            
    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic {self.seed_tag}: {', '.join(self.seed_pieces)}. "
   
    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to generate a set of meaningful {self.goal_tag}s that can be formed out of those {self.seed_tag}. "
    
    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot use the same {self.seed_tag} twice. And you need to use all of {self.seed_tag} on a single {self.goal_tag}. "        
        
    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: [{possible_orderings: [a list of orederings here]} ...]) AND with no extra information or explanation (only the JSON). "
        
        