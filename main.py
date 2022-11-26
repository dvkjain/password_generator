import tkinter as tk
from random import sample as s
root = tk.Tk()

root.title ("Password Generator")
root.geometry ("500x500")
root.configure (bg = "#A4A6D6")


password = ""

characters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
            "E", "F", "G", "H", "I", "J","K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T","U", "V", "W", "X",
            "Y", "Z", "!", "@", "#", "$", "%", "*", "1", "2",
            "3", "4", "5", "6", "7", "8", "9", "0")
class App:

    def __init__(self, master):
        
        self.master = master

        self.password_len = tk.Label (master, width = 30, text = "Enter the amount of characters:", bg = "#A4A6D6", font = "Arial 14 bold")

        self.input_box = tk.Entry (master, bg = "#A4A6D6", borderwidth=0)

        self.generator_button = tk.Button (master, width = 30, height = 2, text = "Generate password", font = "Sans", command = self.password_display, bg = "#A78DC6", highlightthickness = 0)

        self.password_len.pack(pady = 10)
        self.input_box.pack(pady = 10)

        self.generator_button.configure(font = "Arial 12 bold")
        self.generator_button.pack(pady = 10)

    def password_display(self):
            
        # Used an entry to display password
        variable = s (characters, int(self.input_box.get()))
        password = "".join(variable)
        password_final = tk.Entry (root, width = int(self.input_box.get()) + 2, borderwidth = 0, highlightthickness = 0, font = "Arial", readonlybackground = "#A4A6D6")
        password_final.insert (0, password)
        password_final.configure(state = "readonly")
        password_final.pack(pady = 20)

if __name__ == "__main__":

    App(root)
    root.mainloop()
