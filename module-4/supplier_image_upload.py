#! /usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"

for file in os.listdir("./supplier-data/images/"):
    if file.endswith(".jpeg"):
        with open("./supplier-data/images/" + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
