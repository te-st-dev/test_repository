import tkinter as tk
from random import randint




def create_app():
    app = tk.Tk()

    text_widget = tk.Label(app, text="Hello, you are attacked")
    text_widget.pack()
    app.mainloop()

def run_app():
    create_app()