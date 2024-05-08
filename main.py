            #1. BARACK JOHN        - IN16/00030/21      -0703750808    -GROUP LEADER
            #2. KEVIN GUNGA        - IN16/00056/21      -0707168253
            #3. NELSON GATONYE     - IN16/00006/21      -0745806960
            #4. WILKINS OLEKITIENYE-IN16/00041/21       -0795080604
            #5. GRIFFINE OMBOGO    -IN16/00035/21       - 0791947701"





import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Text Editor")

        self.text_area = tk.Text(master, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        master.config(menu=self.menu_bar)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

root = tk.Tk()
text_editor = TextEditor(root)
root.mainloop()
