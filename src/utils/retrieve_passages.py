from src.utils.config.express_server import EXPRESS_SERVER_URL
import requests


def fetch_retrieved_passages(level, module):
    response = requests.get(
        f"{EXPRESS_SERVER_URL}/api/v1/words/get-examples?level={level}&module={module}"
    )

    return response.json().get("data", [])
