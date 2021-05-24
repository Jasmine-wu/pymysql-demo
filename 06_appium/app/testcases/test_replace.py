import yaml
import json


def test_text():
    _params = {}
    _params["company"] = "阿里巴巴"
    _params["code"] = "BABA"


    with open("../step/test_search.yaml", encoding="utf-8") as f:
        steps = yaml.safe_load(f)["search"]
    content = json.dumps(steps)
    print("type :", type(content))
    print("content", content)
    for key, value in _params.items():
        print("${" + key + "}")
        print("value", value)
        # steps = content.replace("${" + key + "}", value)
        content = content.replace("${" + key + "}", value)

    # print(steps)
    print(content)
        # assert "${company}" in content
        # assert "${code}" in content


# def test_1():
#     a = "${123}"
#     b = a.replace("${"+"123"+"}", "78")
#     print(b)