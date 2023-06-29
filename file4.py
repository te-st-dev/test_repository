import tkinter as tk
import random

class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NotRandom Graphs")
        
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()
        
        self.update_graph()

    def update_graph(self):
        self.canvas.delete("all")  # Clear the canvas
        
        x_start = 50
        y_start = 250
        bar_width = 30
        max_height = 200
        
        # Generate random data for the bars
        data = [random.randint(0, max_height) for _ in range(5)]
        
        for i, value in enumerate(data):
            x0 = x_start + (i * bar_width)
            y0 = y_start
            x1 = x0 + bar_width
            y1 = y_start - value
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            self.canvas.create_text(x0+bar_width//2, y1-15, text=str(value))
            
        # Schedule the next update after 1 second (1000 milliseconds)
        self.root.after(1000, self.update_graph)


def create_application():
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()