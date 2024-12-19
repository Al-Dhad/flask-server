from games.order.order_game import OrderGame 
from games.match.match_game import MatchGame
from games.classify.classify_game import ClassifyGame
from games.order__history.order_history_game import OrderHistoricalGame
from games.fill.fill_game import FillGame

games = {
    "order_chars": OrderGame(type_=2),
    "order_words": OrderGame(type_=1), 
    "match_syns": MatchGame(goal_tag=1),
    "match_opps": MatchGame(goal_tag=2),
    "classify": ClassifyGame(),
    "order_his": OrderHistoricalGame(),
    "fill_paragraph": FillGame()
    
}