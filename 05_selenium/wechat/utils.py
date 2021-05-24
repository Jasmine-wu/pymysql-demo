import json
import time


class Utils:

    @classmethod
    def udid(cls):
        return str(time.time()).replace(".", "")



