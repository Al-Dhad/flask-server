
from games.base_game import BaseGame

class FillGame(BaseGame):
    
    def __init__(self):
        super(BaseGame, self).__init__()
        
        self.prompt = ""
        
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
        self.seed_pieces =  ["يأكل", "ينام", "شاهد", "يساعد"]
            
    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those arabic words: {", ".join(self.seed_pieces)}. "
   
    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to generate a paragraph that uses those words. "
    
    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot use the same word twice. "        
        
    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {paragraph: the resulting paragraph}) AND with no extra information or explanation (only the JSON). "
        
        