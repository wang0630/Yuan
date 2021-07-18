import tkinter as tk

import tkmacosx
from tkmacosx import Button as mac_button
from Tcalculator import Tcalculator
from app_const import ComponentType


class Tframe(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._file_name = None
        self._calculator = Tcalculator()
        self.entryMap = {}
        self.buttonMap = {}
        self.labelMap = {}

    def register(self, component_type, key_name, config=None) -> tk.Widget:
        if config is None:
            config = {}
        if component_type == ComponentType.label:
            m = self.labelMap
            elm = tk.Label(**config)
        elif component_type == ComponentType.button:
            m = self.buttonMap
            elm = tkmacosx.Button(**config)
        elif component_type == ComponentType.entry:
            m = self.entryMap
            elm = tk.Entry(**config)
        else:
            raise Exception("component_type provided not available")
        if key_name in m:
            return m[key_name]
        m[key_name] = elm
        return elm

    def get_component(self, component_type, key_name):
        if component_type == ComponentType.label:
            return self.labelMap[key_name]
        elif component_type == ComponentType.entry:
            return self.entryMap[key_name]
        elif component_type == ComponentType.button:
            return self.buttonMap[key_name]

    def render_error_msg(self, err: Exception):
        error_msg_label = self.get_component(ComponentType.label, "errorMsg")
        error_msg_label["text"] = str(err)
        error_msg_label.grid(row=2, columnspan=2, pady=5)

    def set_file(self, file_name):
        if not file_name:
            return
        self._file_name = file_name
        # file_name_label = tk.Label(master=self, text=file_name, bg="#5DBB63", foreground="blue")
        file_name_label = self.register(
            ComponentType.label,
            "file_name_label",
            {
                "master": self,
                "text": file_name,
                "bg": "#5DBB63",
                "foreground": "blue",
            }
        )
        file_name_label.grid(row=0, column=3, pady=5, padx=5)

    def calculate(self):
        try:
            if self._file_name is None:
                raise Exception("Must provide file name before calculation.")
            self._calculator.calculate(self._file_name)
        except Exception as err:
            self.render_error_msg(err)
