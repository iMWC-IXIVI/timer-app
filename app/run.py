from threading import Thread

from time import sleep

from tkinter import Tk, ttk


root = Tk()
root.attributes('-topmost', True)
root.geometry('400x60')
root.resizable(width=False, height=False)
root.overrideredirect(True)


def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')


def start_move(event):
    root.x = event.x
    root.y = event.y


frm = ttk.Frame(root, padding=10)
frm.grid()

frm.bind('<Button-1>', start_move)
frm.bind('<B1-Motion>', move_window)

label = ttk.Label(frm, text='Нажмите на кнопку "Start" для начала секундомера')
label.grid(column=0, row=0)

timer = 0

is_running = True





def thread_func(thread_timer):
    while is_running:

        sleep(1)
        thread_timer += 1

        if not is_running:
            break

        label.config(text=str(thread_timer))


def start_timer():
    global timer, is_running, button_start

    is_running = True

    thread = Thread(target=thread_func, args=(timer, ))

    button_start.grid_remove()

    thread.start()


def stop_timer():
    global is_running, button_start

    label.config(text='Нажмите на кнопку "Start" для начала секундомера')

    button_start.grid()

    is_running = False


button_start = ttk.Button(frm, text='Start', command=start_timer)
button_stop = ttk.Button(frm, text='Stop', command=stop_timer)

button_start.grid(column=0, row=1)
button_stop.grid(column=1, row=1)

root.mainloop()
