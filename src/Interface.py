import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import System
import time
import os


def open_directory():
    directory = filedialog.askdirectory()
    button['state'] = tk.DISABLED
    
    # count total number of files to get default value
    file_count = 0
    for path in os.listdir(directory):
    # check if current path is a file
        if (os.path.isfile(os.path.join(directory, path))):
            file_count += 1
    
    # reassigns number of files to total file count processed if entry box is left blank or negative or too large
    num_files = int(entry.get()) if entry.get().isdigit() and int(entry.get()) <= file_count and int(entry.get()) >= 0 else file_count
    timed_function = timed_execution(System.process_images)
    timed_function(directory, num_files)
    
    
    root.destroy()

"""Records how long given function takes to run"""
def timed_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start the timer
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # End the timer
        duration = end_time - start_time  # Calculate the duration
        print(f"Function '{func.__name__}' took {duration:.4f} seconds to complete.")
        return result
    return wrapper

# Create Window
root = tk.Tk()
root.title("Open a Directory of Images")
root.geometry("700x400")
root['background'] = '#E1CDB3'

#Peter picture :D
cwd = os.path.dirname(os.path.abspath(__file__))
peter_filename = "peter2.png"
peter_path = os.path.join(cwd, peter_filename)
peter = Image.open(peter_path)
peter = peter.resize((250, 200), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(peter)

#image label
image_label = tk.Label(root, image=photo, border=False)
image_label.pack(pady=20)

#Allow entry to number of files to process
entry_label = tk.Label(root, text="Enter number of files to process\nLeave the box blank if you wish to process every file in the folder", bg='#94F7F9')
entry_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create button to open directory
button = tk.Button(root, text="Select a Directory of Images", command=open_directory, bg='#94F7F9')
button.pack(pady=20)


root.mainloop()