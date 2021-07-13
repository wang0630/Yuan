import tkinter as tk


class Window:
    def __init__(self, window: tk.Tk):
        self._window = window

    def run(self) -> None:
        self._window.mainloop()
