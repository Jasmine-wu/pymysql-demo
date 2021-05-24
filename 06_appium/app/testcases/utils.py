import yaml

def load_data(filepath: str, key=None):
    if not filepath.startswith("../data"):
        filepath = "../data/" + filepath
        print(filepath)
    with open(filepath, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if key is None:
        return data
    return data[key]
