import time
import threading
import random
import tkinter as tk

from appwindow import TypeSpeedGUI


# configuration of start function to run on mouse click
def start(event):
    if not app.running:
        if not event.keycode in [16, 17, 18]:
            app.running = True
            t = threading.Thread(target=time_thread)
            t.start()

    # checking the correctness of the user input
    if not app.sample_label.cget('text').startswith(app.input_entry.get()):
        app.input_entry.config(fg='red')
    else:
        app.input_entry.config(fg='black')
    if app.input_entry.get() == app.sample_label.cget('text')[:-1]:
        app.running = False
        app.input_entry.config(fg='green')


# function for time calculations
def time_thread():
    while app.running:
        time.sleep(0.1)
        # count the number of seconds have passed
        app.counter += 0.1
        cps = len(app.input_entry.get()) / app.counter
        cpm = cps * 60
        wps = len(app.input_entry.get().split(' ')) / app.counter
        wpm = wps * 60

        app.speed_label.config(text=f'Speed: \n'
                                    f'{cps:.2f} CPS \n'
                                    f'{cpm:.2f} CPM \n'
                                    f'{wps:.2f} WPS \n'
                                    f'{wpm:.2f} WPM \n')


# functionality of reset button
def reset():
    app.running = False
    app.counter = 0
    app.speed_label.config(text="Speed: \n"
                                "0.00 CPS \n"
                                "0.00 CPM \n"
                                "0.00 WPS \n"
                                "0.00 WPM")
    app.sample_label.config(text=random.choice(app.text))
    app.input_entry.delete(0, tk.END)


# GUI  class assigned to app var
window = tk.Tk()
window.title('Typing speed Tester')
window.geometry('800x600')

app = TypeSpeedGUI(start, reset, window)


window.mainloop()
