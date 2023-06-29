import datetime

def hello_message():
    print("Hello World")

def file_updater():
    with open("/home/client/program_logs/data.txt", "a") as file:
        formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s")
        file.write("I updated file at {formatted_datetime}")