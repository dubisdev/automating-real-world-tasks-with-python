#!/usr/bin/env python3

import shutil, psutil, socket, emails, os

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage <= 80

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_memory_usage():
    mu = psutil.virtual_memory().available
    total = mu / (1024.0 ** 2)
    return total > 500

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def send_email(subject):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)



if not check_cpu_usage():
    subject = "Error - CPU usage is over 80%"
    send_email(subject)

if not check_disk_usage('/'):
    subject = "Error - Available disk space is less than 20%"
    send_email(subject)

if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    send_email(subject)

if not check_localhost():
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    send_email(subject)

