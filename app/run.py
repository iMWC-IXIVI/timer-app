from threading import Thread

from time import sleep

from tkinter import Tk, ttk


root = Tk()
root.attributes('-topmost', True)

frm = ttk.Frame(root, padding=10)
frm.grid()

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
    global timer, is_running

    is_running = True

    thread = Thread(target=thread_func, args=(timer, ))
    thread.start()


def stop_timer():
    global is_running

    label.config(text='Нажмите на кнопку "Start" для начала секундомера')

    is_running = False


ttk.Button(frm, text='Start', command=start_timer).grid(column=0, row=1)
ttk.Button(frm, text='Stop', command=stop_timer).grid(column=1, row=1)

root.mainloop()
