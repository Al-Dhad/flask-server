
from games.base_game import BaseGame

class MatchGame(BaseGame):
    
    tags = {
        1: "synonym",
        2: "opposite"
    }
    
    def __init__(self, goal_tag=1):
        super(BaseGame, self).__init__()
        
        self.prompt = ""
        
        self.goal_tag = self.tags[goal_tag]
        self.seed_pieces = []
        
        self._BaseGame__build_prompt()
        
    def _BaseGame__build_prompt(self):
        self._BaseGame__load_seed_pieces()
        self._BaseGame__prepare_prompt_salt()
        self._BaseGame__prepare_prompt_task()
        self._BaseGame__prepare_prompt_task_notices()
        self._BaseGame__prepare_prompt_pepper()
    
    def _BaseGame__load_seed_pieces(self):
        # normally, we would load those from the DB
        self.seed_pieces =  ["تهوى", "تنظيم", "الوفي", "نجح"]
            
    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {", ".join(self.seed_pieces)}. "
   
    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to generate a single {self.goal_tag} for each of those words. "
    
    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot use the same word twice. "        
        
    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {the given word: the result} with each word in its object) AND with no extra information or explanation (only the JSON). "
        
        