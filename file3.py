import tkinter as tk
import random



# Sample data generation function
def generate_data():
    return random.randint(0, 100)


# Function to update the data and redraw the graph
def update_data():
    # Generate new random data
    data = [generate_data() for _ in range(10)]

    # Clear previous graph
    graph_canvas.delete("all")

    # Calculate dimensions of the canvas
    canvas_width = graph_frame.winfo_width()
    canvas_height = graph_frame.winfo_height()

    # Calculate bar width and gap between bars
    bar_width = canvas_width / len(data)
    bar_gap = bar_width / 4

    # Calculate maximum data value for scaling
    max_value = max(data) if data else 1

    # Draw bars based on the data
    for i, value in enumerate(data):
        # Calculate bar height based on the canvas height and data value
        bar_height = (value / max_value) * canvas_height

        # Calculate bar coordinates
        x1 = i * bar_width + bar_gap
        y1 = canvas_height - bar_height
        x2 = (i + 1) * bar_width - bar_gap
        y2 = canvas_height

        # Draw the bar on the canvas
        graph_canvas.create_rectangle(x1, y1, x2, y2, fill="blue")

    # Schedule the next update after 1 second (adjust the interval as needed)
    root.after(1000, update_data)

def create_app():
    global root, graph_canvas, graph_frame

    # Create the main window
    root = tk.Tk()
    root.title("Dashboard")

    # Create a frame for the graph
    graph_frame = tk.Frame(root, width=400, height=300)
    graph_frame.pack(pady=10)

    # Create a canvas for the graph
    graph_canvas = tk.Canvas(graph_frame, bg="white")
    graph_canvas.pack(fill=tk.BOTH, expand=True)

    # Schedule the initial update after 1 second
    root.after(1000, update_data)

    # Start the Tkinter event loop
    root.mainloop()
