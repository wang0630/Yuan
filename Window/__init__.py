import tkinter as tk
from tkmacosx import Button as mac_button
from Tframe import Tframe
from tkinter.filedialog import askopenfilename
from app_const import ComponentType


class Window:
    def __init__(self, window: tk.Tk):
        self._window = window

    def run(self) -> None:
        self._window.geometry("500x500")
        self._window.configure(bg="#49A")
        padding = {'padx': 5, 'pady': 5}
        input_text = ["File name"]
        frame = Tframe(master=self._window, borderwidth=1, bg="#5DBB63")
        for index, text in enumerate(input_text):
            label_a = tk.Label(master=frame, text=text, bg="#5DBB63", foreground="blue")
            frame.register("fileName", label_a)
            label_a.grid(row=0, column=0, **padding)
            label_b = tk.Label(master=frame, text=text, bg="#5DBB63", foreground="blue")
            frame.register("errorMsg", label_b)
            # entry = tk.Entry(master=frame)
            # frame.register("fileName", entry)
            # entry.grid(row=0, column=1, **padding)

        file_button = mac_button(
            master=frame,
            text="Calculate",
            fg="black",
            command=lambda: frame.calculate(askopenfilename())
        )

        frame.register("calculate", file_button)
        # span two columns (0 ~ 1)
        file_button.grid(row=0, column=2, columnspan=2, pady=5)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self._window.mainloop()
