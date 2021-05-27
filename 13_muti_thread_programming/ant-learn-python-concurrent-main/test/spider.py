import requests

url = [f"https://www.cnblogs.com/#p{page}" for page in range(0, 50)]


def craw(url):
    res = requests.get(url)
    return res
