import os.path
import random
import time
import threading
import tkinter
import tkinter as tk


# Function to log messages to log list
def log(message: str):
    log_list.insert(tk.END, message)
    log_list.yview(tk.END)


def feed():
    log("Feed")  # Placeholder


def shop():
    log("Shop")  # Placeholder


# Initialise window and define title, geometry
root = tk.Tk()
root.title("The Virtual Pet Game")
root.geometry("500x500")

# Labels for displaying levels. Constantly updating
hunger_label = tk.Label(root, text="Hunger:")
thirst_label = tk.Label(root, text="Thirst:")
happiness_label = tk.Label(root, text="Happiness:")
money_label = tk.Label(root, text="Money:")
hunger_label.pack()
thirst_label.pack()
happiness_label.pack()
money_label.pack()

# Create log box with scrollbar
log_frame = tk.Frame(root)
scrollbar = tk.Scrollbar(log_frame, orient="vertical")  # Create scrollbar on framework
log_list = tk.Listbox(log_frame, height=15, width=50, yscrollcommand=scrollbar.set)  # Create log box
scrollbar.config(command=log_list.yview)  # Configure scrollbar to scroll log box
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_list.pack(side=tk.LEFT, fill=tk.BOTH)
log_list.pack()
log_frame.pack()

# Buttons for commands
feed_button = tk.Button(root, text="Feed", command=feed)
shop_button = tk.Button(root, text="Shop", command=shop)
feed_button.pack()
shop_button.pack()

tkinter.mainloop()
