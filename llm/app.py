from flask import jsonify, Flask, request, make_response

from utils.llama_handler import ask_llm_handler, get_tip_from_llm

from errors.non_formatted_input import input_non_valid_error
from errors.status import status
import requests

app = Flask(__name__)

@app.route("/build-game", methods=["GET"])
def build_game():
    response = get_tip_from_llm()

    return make_response(
        jsonify({"data": {"llm_response": response}}), status["success"]
    )

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")
