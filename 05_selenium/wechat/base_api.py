import inspect
import json
from string import Template

import chevron
import requests
import yaml

import ast


class BaseApi():
    def send(self, data: dict):

        if "data" in data.keys():
            dic = ast.literal_eval(data["data"])
            dic = json.dumps(dic).encode("utf-8")
            data["data"] = dic

        return requests.request(**data).json()

    def send_encrypt(self):

        pass

    def load(self, file: str):
        with open(file) as f:
            data = yaml.safe_load(f)
        return data

    def get_step(self, data: dict, name):
        step = data[name]
        return json.dumps(step)

    def append(self, file, data):
        with open(file, "a", encoding="utf-8") as f:
            f.write(yaml.dump(data))

    def template(self, step, data: dict):
        if "$" in step:
            res = Template(step).substitute(data)
        else:
            res = chevron.render(step, data=data)
        return json.loads(res)

    def get_data(self, file, data):
        file = self.load(file)
        func_name = inspect.stack()[1].function
        step = self.get_step(file, func_name)
        return self.template(step, data)
