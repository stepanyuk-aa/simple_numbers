from datetime import datetime

def connect_to_file():
    """Open logs file"""
    file = open('logs.txt', 'a')
    return file

def add_log(text, time = False):
    file = connect_to_file()
    if time:
        file.write(str(datetime.now()) + "\t" + text + "\n")
        print(str(datetime.now()) + "\t" + text + "\n")
    else:
        file.write(text + "\n")
        print(text + "\n")

    file.close()