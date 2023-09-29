#!/usr/bin/env python3

from PIL import Image
import os, glob

target_size = 128, 128
folder = "/opt/icons/"

for infile in glob.glob("./images/*"):
    file = os.path.splitext(infile)

    with Image.open(infile) as im:
        # print(file)
        file_name = file.split("/")[-1]

        target_file_name = folder + file_name
        im.rotate(90).resize(target_size).convert("RGB").save(target_file_name + ".jpeg")
