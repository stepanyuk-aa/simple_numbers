from datetime import datetime

def connect_to_file():
    """Open logs file"""
    file = open('logs.txt', 'a')
    return file

def add_log(text, time = False):
    file = connect_to_file()
    if time:
        file.write(str(datetime.now()) + "\t" + text + "\n")
        print(str(datetime.now()) + "\t" + text)
    else:
        file.write(text + "\n")
        print(text)

    file.close()

def add_header():
    add_log(
        "Simple numbers,Computation time,Work time"
    )

def mark_time():
    return datetime.now()

def dif_time(mark1, mark2):
    return str(mark2 - mark1)

