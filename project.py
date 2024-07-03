import tkinter as tk
import tkinter.messagebox as messagebox
import time

# Bubble Sort Algorithm with Animation
def bubble_sort_animation(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                display_text(arr, j, j+1)
                time.sleep(1)
                window.update()
    sorted_list = ', '.join(map(str, arr))
    messagebox.showinfo("Sorted List", f"Sorted List: {sorted_list}")

# Function to display numbers with color highlighting on canvas
def display_text(arr, idx1, idx2):
    canvas.delete("text")
    text_width = len(arr) * 50  # Calculate the total width of the text
    x = (canvas_width - text_width) / 2  # Center the list horizontally
    y = message_coords[1] + 70  # Set y-coordinate below the message
    for idx, val in enumerate(arr):
        if idx == idx1 or idx == idx2:
            color = "red"
        else:
            color = "black"
        canvas.create_text(x, y, text=str(val), fill=color, font=("Arial", 20), tag="text")
        x += 50  # Adjust the horizontal spacing between numbers

# Function to handle sorting button click
def handle_sort_algorithm():
    input_text = input_text_widget.get("1.0", "end-1c")
    arr = [int(elem) for elem in input_text.split(',')]
    bubble_sort_animation(arr.copy())

# Create a Tkinter window
window = tk.Tk()
window.title("Sorting Algorithm Animations")
window.geometry("600x500")

# Create a frame for better organization
frame = tk.Frame(window)
frame.pack(pady=20)

# Create a canvas for displaying text and animation
canvas_width = 600
canvas_height = 250
canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Add message above the canvas
message = "How to sort your list👇🏻"
message_coords = (300, 40)  # Coordinates of the message
canvas.create_text(*message_coords, text=message, fill="blue", font=("Arial", 18), tag="message")

# Create a label for input message
input_msg_label = tk.Label(frame, text="Enter numbers separated by commas:", font=("Arial", 14))
input_msg_label.pack(pady=10)

# Create a text widget for user input
input_text_widget = tk.Text(frame, height=2, width=50, font=("Arial", 14))
input_text_widget.pack()

# Create a button for sorting
sort_button = tk.Button(frame, text="Sort", command=handle_sort_algorithm, bg="blue", fg="white", font=("Arial", 14))
sort_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop() 