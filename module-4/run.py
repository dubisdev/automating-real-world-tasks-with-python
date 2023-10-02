#! /usr/bin/env python3

import os
import requests

# Iterate over files in the supplier-data/descriptions/ directory
fruit_data = []

for file in os.listdir("./supplier-data/descriptions/"):
    # Open each file and read the data
    with open("./supplier-data/descriptions/" + file, "r") as f:
        fruit = {}
        lines = f.readlines()
        # Read the data from each line and assign it to the appropriate key
        fruit["name"] = lines[0].rstrip("\n")
        # Here we remove the lbs from the weight
        fruit["weight"] = int(lines[1].rstrip("\n").split(" ")[0])
        fruit["description"] = lines[2].rstrip("\n")
        fruit["image_name"] = file.replace("txt", "jpeg")

        # Append the data to the list
        fruit_data.append(fruit)

# POST every fruit to the website

for fruit in fruit_data:
    response = requests.post("http://localhost/fruits/", json=fruit)
    print(response.status_code)
