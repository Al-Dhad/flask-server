import json_repair


def repair_json(bad_json):
    return json_repair.loads(bad_json)