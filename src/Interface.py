import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox as mb 
from PIL import Image, ImageTk
import System
import time
import os

csv_path = None
DESCRIPTIONS = False

def open_directory():
    global csv_path
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
    timed_function(directory, csv_path, num_files, DESCRIPTIONS)
    
    
    root.destroy()

def select_csv():
    global csv_path
    csv_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if csv_path:
        csv_button['state'] = tk.DISABLED
    button['state'] = tk.NORMAL

def toggle_descriptions():
    res = mb.askquestion("Descriptions", "Turn on artwork descriptions?") 
      
    if res == 'yes':
        DESCRIPTIONS = True
    else:
        DESCRIPTIONS = False
    
# Records how long given function takes to run
def timed_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start the timer
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # End the timer
        duration = end_time - start_time  # Calculate the duration
        print(f"Function '{func.__name__}' took {duration:.4f} seconds to complete. Keyword Results are stored in image_data.csv")
        return result
    return wrapper

# Create Window
root = tk.Tk()
root.title("Open a Directory of Images")
root.geometry("700x400")
root['background'] = '#E1CDB3'

#Peter picture :D
# cwd = os.path.dirname(os.path.abspath(__file__))
# peter_filename = "peter2.png"
# peter_path = os.path.join(cwd, peter_filename)
# peter = Image.open(peter_path)
# peter = peter.resize((250, 200), Image.Resampling.LANCZOS)
# photo = ImageTk.PhotoImage(peter)

# #image label
# image_label = tk.Label(root, image=photo, border=False)
# image_label.pack(pady=20)

# Create button to toggle descriptions on/off
desc_button = tk.Button(root, text="Turn on Descriptions?", command=toggle_descriptions, bg='#FECC07', font=("Helvetica", 16))
desc_button.pack(pady = 2)

#Allow entry to number of files to process
entry_label = tk.Label(root, text="1. Enter Number of Images to Process\n(Leave the box blank if you wish to process every file in the folder)",fg='#FECC07', bg='#255799', font=("Helvetica", 16))
entry_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

# Create button to input csv file
csv_button = tk.Button(root, text="2. Select Keywords CSV File", command=select_csv, bg='#FECC07', font=("Helvetica", 16))
csv_button.pack(pady=10)

# Disable csv button then enable select Directory button

# Create button to open directory
button = tk.Button(root, text="3. Select a Directory of Images to Process", command=open_directory, fg='#FECC07', bg='#255799', font=("Helvetica", 16))
button['state'] = tk.DISABLED

button.pack(pady=20)


root.mainloop()