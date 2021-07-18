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
        frame = Tframe(master=self._window, borderwidth=1, bg="#5DBB63")
        label = frame.register(
            ComponentType.label,
            "fileName",
            {
                "master": frame,
                "text": "File name",
                "bg": "#5DBB63",
                "foreground": "blue"
            }
        )
        label.grid(row=0, column=0, **padding)
        vd_constraints_label = frame.register(
            ComponentType.label,
            "vd_constraints",
            {
                "master": frame,
                "text": "Vd constraints, use x,y,z format",
                "bg": "#5DBB63",
                "foreground": "blue"
            }
        )
        vd_constraints_label.grid(row=1, columnspan=2, **padding)
        # Error msg
        error_msg_label = frame.register(ComponentType.label, "errorMsg", {
            "master": frame,
            "bg": "#5DBB63",
            "foreground": "red",
        })

        file_button = frame.register(ComponentType.button, "file_button", {
            "master": frame,
            "text": "Choose a file",
            "fg": "black",
            "command": lambda: frame.set_file(askopenfilename())
        })
        calculate_button = frame.register(ComponentType.button, "calculate_button", {
            "master": frame,
            "text": "Calculate",
            "fg": "black",
            "command": lambda: frame.calculate()
        })
        # span two columns (0 ~ 1)
        file_button.grid(row=0, column=1, columnspan=2, pady=5)
        calculate_button.grid(row=3, columnspan=2, pady=5)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self._window.mainloop()
