#!/usr/bin/env python3

import glob, requests

server_ip = "0.0.0.0" # Replace with the server IP

all_feedback = []
for file in glob.glob("/data/feedback/*.txt"):
    with open(file) as file:
        lines = file.readlines()
        data = {"title": lines[0].strip(),
                "name": lines[1].strip(),
                "date": lines[2].strip(),
                "feedback": lines[3].strip()}
        all_feedback.append(data)

for feedback in all_feedback:
    response = requests.post(f"http://{server_ip}/feedback/", json=feedback)

    print(response.status_code)

    if not response.ok:
        print(response.text)
