import datetime
import time

def hello_message():
    print("Hello World")
    infinity_printer()

def file_updater():
    with open("/home/client/program_logs/data.txt", "a") as file:
        formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s")
        file.write("I updated file at {}\n".format(formatted_datetime))

def infinity_printer():
    while True:
        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s"))
        time.sleep(4)