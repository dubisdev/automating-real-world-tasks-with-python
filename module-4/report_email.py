#!/usr/bin/env python3

import reports, emails
import datetime
import os

def get_data():
    # Iterate over files in the supplier-data/descriptions/ directory
    fruit_data = []

    for file in os.listdir("./supplier-data/descriptions/"):
        # Open each file and read the data
        with open("./supplier-data/descriptions/" + file, "r") as f:
            fruit = {}
            lines = f.readlines()
            # Read the data from each line and assign it to the appropriate key
            fruit["name"] = lines[0].rstrip("\n")
            fruit["weight"] = lines[1]

            # Append the data to the list
            fruit_data.append(fruit)

    return fruit_data

def generate_paragraph(fruit_data):
    paragraph = ""

    for fruit in fruit_data:
        paragraph += "name: " + fruit["name"] + "<br/>"
        paragraph += "weight: " + fruit["weight"] + "<br/><br/>"

    return paragraph

if __name__ == "__main__":
    fruit_data = get_data()
    paragraph = generate_paragraph(fruit_data)
    file_path = "/tmp/processed.pdf"
    title = "Processed Update on {}".format(datetime.date.today())


    reports.generate_report(file_path, title, paragraph)

    sender = "automation@example.com"
    recipient = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    mail = emails.generate_email(sender, recipient, subject, body, file_path)
    emails.send_email(mail)
