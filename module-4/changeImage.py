#!/usr/bin/env python3

from PIL import Image
import os, glob

for file in os.listdir("./supplier-data/images/"):
    if file.endswith(".tiff"):
        file_name = file.split(".")[0]
        im = Image.open("./supplier-data/images/" + file)
        im.resize((600, 400)).convert("RGB").save("./supplier-data/images/" + file_name + ".jpeg")
        im.close()
