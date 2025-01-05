from flask import jsonify, Flask, request, make_response

from src.utils.llama_handler import llm_query_handler, ask_llm_replicate

from src.games.factory.game_factory import games

from src.errors.non_formatted_input import input_non_valid_error
from src.errors.status import status

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/build-game", methods=["GET"])
def build_game():
    game_type = request.args.get("game_type")
    level = request.args.get("level")
    module = request.args.get("module")

    if not game_type or game_type not in games.keys():
        return make_response(
            jsonify(error=input_non_valid_error), status["input_not_valid"]
        )

    game = games[game_type]

    game._BaseGame__build_prompt(level, module)
    
    print(game.prompt)

    response = ask_llm_replicate(game.prompt)

    response_data = {"llm_response": response}
    if hasattr(game, "seed_pieces"):
        response_data["seed_pieces"] = game.seed_pieces

    return make_response(jsonify({"data": response_data}), status["success"])

# if __name__ == "__main__":
app.run(debug=False, port=10000, host="0.0.0.0")
