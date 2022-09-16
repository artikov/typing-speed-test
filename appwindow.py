import random
import tkinter as tk


class TypeSpeedGUI:
    def __init__(self, start, reset, window):
        self.text = open('data.txt', 'r').read().split('\n')

        self.frame = tk.Frame(window)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.text), font=('Arial', 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=('Arial', 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        # function to start automatically when key is pressed
        self.input_entry.bind('<KeyPress>', start)

        # timer label
        self.speed_label = tk.Label(self.frame, text="Speed: \n"
                                                     "0.00 CPS \n"
                                                     "0.00 CPM \n"
                                                     "0.00 WPS \n"
                                                     "0.00 WPM",
                                    font=('Arial', 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        # reset button
        self.reset_button = tk.Button(self.frame, text='Reset', command=reset, font=('Arial', 24))
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        # check if app is started or not
        self.counter = 0
        self.running = False





