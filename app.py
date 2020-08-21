from tkinter import *
import time

# import filedialog module
from tkinter import filedialog
from tkinter import messagebox

class Paths:
        def __init__(self):
            self.input = None
            self.output = None

def main():
    # Function for opening the
    # file explorer window
    def browse_files_input(obj):
        filename = filedialog.askdirectory(initialdir="/")
        obj.input = filename
        # Change label contents
        label_file_explorer_input.configure(text="Input folder: " + filename)

    def browse_files_output(obj):
        filename = filedialog.askdirectory(initialdir="/")
        obj.output = filename
        # Change label contents
        label_file_explorer_output.configure(text="Output folder: " + filename)

    # Create the root window
    window = Tk()
    paths = Paths()

    # Set window title
    window.title('File Explorer')

    # Set window size
    window.geometry("360x400")

    # Set window background color
    window.config(background="white")

    # Create a File Explorer label
    label_file_explorer_input = Label(window,
                                text="Select input directory:",
                                width=50, height=3,
                                fg="blue")

    button_explore_input = Button(window,
                            text="Browse Folder",
                            command=lambda: browse_files_input(paths))

    label_file_explorer_output = Label(window,
                                text="Select output directory:",
                                width=50, height=3,
                                fg="blue")

    button_explore_output = Button(window,
                            text="Browse Folder",
                            command=lambda: browse_files_output(paths))


    # Grid method is chosen for placing
    # the widgets at respective positions
    # in a table like structure by
    # specifying rows and columns
    label_file_explorer_input.grid(column=1, row=1)
    button_explore_input.grid(column=1, row=2)
    label_file_explorer_output.grid(column=1, row=5)
    button_explore_output.grid(column=1, row=6)

    def resize(scale):
        if paths.input is None:
            messagebox.showerror("error", "Input folder must be selected!")
            return
        if paths.output is None:
            messagebox.showerror("warnings", "Output folder should be selected!")
        info_msg.set("Resize has started")
        time.sleep(20)
        # call the processing
        # info_msg.set("Resize has ended")
        return

    def resize_x2():
        resize(2)

    def resize_x4():
        resize(4)

    # create the buttons
    x2_button = Button(window, text ="Resize x2", command=resize_x2)
    x2_button.grid(column=1, row=8)
    x4_button = Button(window, text ="Resize x4", command=resize_x4)
    x4_button.grid(column=1, row=9)

    # showing info
    info_msg = StringVar()
    info_msg.set("")
    label_info = Label(window, textvariable=info_msg)
    label_info.grid(column=1, row=10)

    # Let the window wait for any events
    window.mainloop()

main()