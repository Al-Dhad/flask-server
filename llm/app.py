from flask import jsonify, Flask, request, make_response

from utils.llama_handler import llm_query_handler

from games.factory.game_factory import games

from errors.non_formatted_input import input_non_valid_error
from errors.status import status
import requests

app = Flask(__name__)

@app.route("/build-game", methods=["GET"])
def build_game():
    game_type = request.args.get('game_type')

    if not game_type or game_type not in games.keys():
        return make_response(jsonify(error=input_non_valid_error), status["input_not_valid"])
    
    game = games[game_type]
    
    response = llm_query_handler(game.prompt)

    return make_response(
        jsonify({"data": {"llm_response": response}}), status["success"]
    )

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
