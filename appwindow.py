import random
import tkinter as tk


class TypeSpeedGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Typing speed Tester')
        self.window.geometry('800x600')

        self.text = open('data.txt', 'r').read().split('\n')

        self.frame = tk.Frame(self.window)

        self.sample_label = tk.Label(self.window, text=random.choice(self.text), font=('Ariel', 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=('Ariel', 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        # function to start automatically when key is pressed
        # self.input_entry.bind('<KeyPress>', self.start)



