from os import readlink
from tkinter import *
import tkinter.filedialog as fd
from text_editor_main import EditBuffer

class TextEditor:
    def __init__(self):
        self.window = Tk()
        self.window.title('My Text Editor')
        self.text = Text(self.window, wrap=WORD)
        self.text.pack(fill="none", expand=TRUE)
        menu = Menu(self.window)
        self.window.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Options', menu=filemenu)
        filemenu.add_command(label='New', command=self.NewFile)
        filemenu.add_separator()
        filemenu.add_command(label='Open', command=self.OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label='Save', command=self.SaveFile)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.window.destroy)
        self.buffer = EditBuffer()   # Edit Buffer ADT

    def NewFile(self):
        self.window.destroy()
        self.__init__()

    def OpenFile(self):
        filename = fd.askopenfilename()
        self.NewFile()
        self.buffer.EditFile(filename)
        self.text.insert(INSERT, self.buffer.__str__())

    def SaveFile(self):
        lines = self.text.get(1.0, END).split()
        if self.buffer.FileName == None:
            self.buffer.FileName = fd.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
        self.buffer.CreateNewFile(self.buffer.FileName)
        for line in lines:
            self.buffer.InsertLine(line)
        self.buffer.SaveFile()
        
    def main(self):
        self.window.mainloop()


# Driver Code
editor = TextEditor()
editor.main()
