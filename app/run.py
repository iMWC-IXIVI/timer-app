from threading import Thread

from tkinter import Tk, ttk, Frame

from time import sleep
from datetime import datetime, timedelta


root = Tk()
root.attributes('-topmost', True)
root.geometry('100x50')
root.resizable(width=False, height=False)
root.overrideredirect(True)


def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')


def start_move(event):
    root.x = event.x
    root.y = event.y


# frm = ttk.Frame(root, padding=10)
frm = Frame(root)
frm.pack(fill='both', expand=True)

frm.bind('<Button-1>', start_move)
frm.bind('<B1-Motion>', move_window)

label = ttk.Label(frm, text='Секундомер')
label.place(x=10, y=0)

timer = datetime.strptime('00:00:00', '%H:%M:%S')
is_running = True


def thread_func():
    global timer

    label.place(x=27, y=0)

    while is_running:

        if not is_running:
            break

        timer += timedelta(seconds=1)

        label.config(text=f'{timer.time()}')

        sleep(1)


def start_timer():
    global timer, is_running, button_start, button_stop

    is_running = True

    thread = Thread(target=thread_func)

    button_start.place_forget()
    button_stop.place(x=0, y=25)

    thread.start()


def stop_timer():
    global is_running, button_start, button_stop, timer

    is_running = False

    label.config(text=f'{timer.time()}')
    label.place(x=27, y=0)

    button_start.place(x=0, y=25)
    button_stop.place_forget()

    timer = datetime.strptime('00:00:00', '%H:%M:%S')


button_start = ttk.Button(frm, text='▶', command=start_timer, width=5)
button_stop = ttk.Button(frm, text='■', command=stop_timer, width=5)
button_exit = ttk.Button(frm, text='Exit', command=root.destroy, width=5)

button_start.place(x=0, y=25)
button_exit.place(x=60, y=25)

root.mainloop()
