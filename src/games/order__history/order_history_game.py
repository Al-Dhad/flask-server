
from games.base_game import BaseGame

class OrderHistoricalGame(BaseGame):

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
        self.seed_pieces =  ["november 1954", "july 1962", "july 1830"]
            
    def _BaseGame__prepare_prompt_salt(self):
        self.prompt += f"Given those Algerian historical events: {", ".join(self.seed_pieces)}. "
   
    def _BaseGame__prepare_prompt_task(self):
        self.prompt += f"You are asked to order those events, while giving a brief explanation to what happened in each event in arabic. "
    
    def _BaseGame__prepare_prompt_task_notices(self):
        self.prompt += f"Please note the following: you cannot use the same event twice. "        
        
    def _BaseGame__prepare_prompt_pepper(self):
        self.prompt += "Return ONLY your answer in JSON format (having the following format: {event_i: {date, order_indice, description}}) AND with no extra information or explanation (only the JSON). "
        
        