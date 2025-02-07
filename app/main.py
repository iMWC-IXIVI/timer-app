from threading import Thread

from tkinter import Tk, Label, Button, Frame

from datetime import datetime, timedelta
from time import sleep


class TimerApp(Tk):
    def __init__(self):
        self.frame = None
        self.label = None
        self.button_start = None
        self.button_stop = None
        self.button_exit = None
        self.is_running = None

        self.window_x = 100
        self.window_y = 50
        self.back_color = 'black'
        self.front_color = 'yellow'
        self.timer = datetime.strptime('00:00:00', '%H:%M:%S')

        super().__init__()
        self.__setting_app()
        self.main_frame()
        self.main_label()
        self.button_definition()

    def __setting_app(self):
        self.geometry(f'{self.window_x}x{self.window_y}+{self.__screen_setting()}+{0}')
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.__hide_back_display()

    def __screen_setting(self):
        screen_x = self.winfo_screenwidth()
        return screen_x - self.window_x

    def __hide_back_display(self):
        self.configure(bg=self.back_color)
        self.attributes('-transparentcolor', self.back_color)

    def main_frame(self):
        self.frame = Frame(self, bg=self.back_color)
        self.frame.pack(fill='both', expand=True)

    def main_label(self):
        self.label = Label(self.frame, text='Секундомер', bg=self.back_color, fg=self.front_color, font=('', 10))
        self.label.place(x=10, y=0)

    def __buttons(self):
        self.button_start = Button(self.frame, text='▶', command=self.start_timer, width=3, bg=self.back_color, fg=self.front_color)
        self.button_stop = Button(self.frame, text='■', command=self.stop_timer, width=3, bg=self.back_color, fg=self.front_color)
        self.button_exit = Button(self.frame, text='Exit', command=self.destroy, width=3, bg=self.back_color, fg=self.front_color)

    def button_definition(self):
        self.__buttons()

        self.button_start.place(x=0, y=25)
        self.button_exit.place(x=68, y=25)

    def start_timer(self):
        self.is_running = True

        thread = Thread(target=self.__thread_timer)

        self.button_start.place_forget()
        self.button_stop.place(x=0, y=25)

        thread.start()

    def __thread_timer(self):
        self.label.place(x=27, y=0)

        while self.is_running:
            if not self.is_running:
                break

            self.timer += timedelta(seconds=1)
            self.label.config(text=f'{self.timer.time()}')
            sleep(1)

    def stop_timer(self):
        self.is_running = False

        self.label.config(text=f'{self.timer.time()}')
        self.label.place(x=27, y=0)

        self.button_start.place(x=0, y=25)
        self.button_stop.place_forget()

        self.timer = datetime.strptime('00:00:00', '%H:%M:%S')

    def run_app(self):
        self.mainloop()


if __name__ == '__main__':
    app = TimerApp()
    app.run_app()
