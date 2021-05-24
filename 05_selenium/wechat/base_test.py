import json


class BaseTest():
    def print_json(self, data: dict):
        print(json.dumps(data, indent=2, ensure_ascii=False))
