from abc import ABC, abstractmethod

class BaseGame(ABC):
    
    def __init__(self):
        self.prompt = ""
    
    @abstractmethod
    def __build_prompt(self, level, module):
        pass
    
    @abstractmethod
    def __load_seed_pieces(self, level, module):
        pass

    @abstractmethod
    def __prepare_prompt_salt(self):
        pass
    @abstractmethod
    def __prepare_prompt_task(self):
        pass
    
    @abstractmethod
    def __prepare_prompt_task_notices(self):
        pass
            
    @abstractmethod
    def __prepare_prompt_pepper(self):
        pass        
        
