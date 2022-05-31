import requests
import os
from page_loader.lib.works_name import name_formation


def download(_url, _path):
    req = requests.get(_url)
    src = req.text
    name_file = os.path.join(_path, name_formation(_url) + '.html')
    with open(name_file, "w") as file:
        file.write(src)
    return name_file
