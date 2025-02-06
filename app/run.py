from threading import Thread

from time import sleep

from tkinter import Tk, ttk


root = Tk()
root.attributes('-topmost', True)
root.geometry('500x60')
root.resizable(width=False, height=False)
root.overrideredirect(True)


def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')


def start_move(event):
    root.x = event.x
    root.y = event.y


frm = ttk.Frame(root, padding=10)
frm.pack(fill='both', expand=True)

frm.bind('<Button-1>', start_move)
frm.bind('<B1-Motion>', move_window)

label = ttk.Label(frm, text='Нажмите на кнопку "Start" для начала секундомера')
label.place(x=0, y=0)

timer = 0

is_running = True


def thread_func():
    global timer

    while is_running:

        timer += 1

        label.config(text=str(timer))

        if not is_running:
            break

        sleep(1)


def start_timer():
    global timer, is_running, button_start, button_stop

    is_running = True

    thread = Thread(target=thread_func)

    button_start.place_forget()
    button_stop.place(x=400, y=25)

    thread.start()


def stop_timer():
    global is_running, button_start, button_stop, timer

    label.config(text='Нажмите на кнопку "Start" для начала секундомера')

    button_start.place(x=400, y=25)
    button_stop.place_forget()

    timer = 0
    is_running = False


button_start = ttk.Button(frm, text='Start', command=start_timer, width=5)
button_stop = ttk.Button(frm, text='Stop', command=stop_timer, width=5)
button_exit = ttk.Button(frm, text='Exit', command=root.destroy, width=5)

button_start.place(x=400, y=25)
button_exit.place(x=450, y=25)

root.mainloop()
