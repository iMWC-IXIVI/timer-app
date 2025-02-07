from tkinter import Tk, Label, Button, Frame

from datetime import datetime, timedelta


class TimerApp(Tk):
    def __init__(self):
        super().__init__()
        # Базовые настройки приложения
        self.is_running = False
        self.window_x = 100
        self.window_y = 50
        self.back_color = 'black'
        self.front_color = 'yellow'
        self.timer = datetime.strptime('00:00:00', '%H:%M:%S')
        # Инициализация главного Фрейма, Надписи и Кнопок
        self.frame = Frame(self, bg=self.back_color)
        self.label = Label(self.frame, text='Секундомер', bg=self.back_color, fg=self.front_color, font=('', 10))
        self.button_start = Button(self.frame, text='▶', command=self.start_timer, width=3, bg=self.back_color, fg=self.front_color)
        self.button_stop = Button(self.frame, text='■', command=self.stop_timer, width=3, bg=self.back_color, fg=self.front_color)
        self.button_exit = Button(self.frame, text='Exit', command=self.destroy, width=3, bg=self.back_color, fg=self.front_color)
        # Во время инициализации необходимые настройки приложения
        self.__setting_app()
        self.__frame_setting()
        self.__label_setting()
        self.__button_setting()

    def __setting_app(self):
        """Расположение окна, сокрытие рамок и сокрытие заднего фона"""
        self.geometry(f'{self.window_x}x{self.window_y}+{self.__screen_setting()}+{0}')
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.__hide_back_display()

    def __screen_setting(self):
        """Расположение окна приложения (Правый верхний угол)"""
        screen_x = self.winfo_screenwidth()
        return screen_x - self.window_x

    def __hide_back_display(self):
        """Сокрытие заднего фона приложения (Цвет чёрный)"""
        self.configure(bg=self.back_color)
        self.attributes('-transparentcolor', self.back_color)

    def __frame_setting(self):
        """Увеличиваем рабочую область Фрейма на всё окно"""
        self.frame.pack(fill='both', expand=True)

    def __label_setting(self):
        """Расположение Надписи"""
        self.label.place(x=10, y=0)

    def __button_setting(self):
        """Расположение кнопок"""
        self.button_start.place(x=0, y=25)
        self.button_exit.place(x=68, y=25)

    def start_timer(self):
        """Запуск секундомера"""
        self.is_running = True
        # Сокрытие кнопки "Старт" и раскрытие кнопки "Стоп"
        self.button_start.place_forget()
        self.button_stop.place(x=0, y=25)
        # Обновление таймера
        self.__timer_update()

    def __timer_update(self):
        """Обновление таймера каждую секунду"""
        if self.is_running:
            self.timer += timedelta(seconds=1)
            self.label.config(text=f'{self.timer.time()}')
            self.after(1000, self.__timer_update)

    def stop_timer(self):
        """Остановка таймера"""
        self.is_running = False
        # Замены Надписи и смена расположения надписи
        self.label.config(text=f'{self.timer.time()}')
        self.label.place(x=27, y=0)
        # Раскрытие кнопки "Старт", сокрытие кнопки "Стоп"
        self.button_start.place(x=0, y=25)
        self.button_stop.place_forget()
        # Установка секундомера в начальную точку
        self.timer = datetime.strptime('00:00:00', '%H:%M:%S')

    def run_app(self):
        """Запуск приложения"""
        self.mainloop()


if __name__ == '__main__':
    app = TimerApp()
    app.run_app()
