from games.order.order_game import OrderGame 
from games.match.match_game import MatchGame
from games.classify.classify_game import ClassifyGame

games = {
    "order_chars": OrderGame(type_=2),
    "order_words": OrderGame(type_=1), 
    "match_syns": MatchGame(goal_tag=1),
    "match_opps": MatchGame(goal_tag=2),
    "classify": ClassifyGame(),
    
}