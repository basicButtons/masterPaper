import ujson
import json


def saveIndex(index: int):
    index = {"index": index}
    with open('./test.json', 'w') as f:
        ujson.dump(index, f)


def loadIndex():
    content = ""
    with open('test.json', 'r') as f:
        for line in f:
            content = content + line
    res = json.loads(content)
    index = res["index"]
    return index


loadIndex()
