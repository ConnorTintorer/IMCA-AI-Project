import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import System



def open_directory():
    directory = filedialog.askdirectory()
    System.process_images(directory)


def interface_loop():
    # Create Window
    root = tk.Tk()
    root.title("Open a Directory of Images")
    root.geometry("700x300")
    
    #Peter picture :D
    peter_path = "C:/Users/conno/IMCATestProject/misc/peter.png"
    peter = Image.open(peter_path)
    peter = peter.resize((200, 200), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(peter)
    
    #image label
    image_label = tk.Label(root, image=photo)
    image_label.pack(pady=20)
    
    
    # Create button to open directory
    button = tk.Button(root, text="Select a Directory of Images", command=open_directory)
    button.pack(pady=20)
    
    
    root.mainloop()
    
if __name__ == '__main__':
    interface_loop()