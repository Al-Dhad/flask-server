from src.games.order.order_game import OrderGame 
from src.games.match.match_game import MatchGame
from src.games.classify.classify_game import ClassifyGame
from src.games.order__history.order_history_game import OrderHistoricalGame
from src.games.fill.fill_game import FillGame

games = {
    "order_chars": OrderGame(type_=2), #
    "order_words": OrderGame(type_=1), #
    "match_syns": MatchGame(goal_tag=1), #
    "match_opps": MatchGame(goal_tag=2), #
    "classify": ClassifyGame(), #
    "order_his": OrderHistoricalGame(),
    "fill_paragraph": FillGame() #
    
}