import tkinter as tk
from Tcalculator import Tcalculator
from app_const import ComponentType


class Tframe(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._calculator = Tcalculator()
        self.entryMap = {}
        self.buttonMap = {}
        self.labelMap = {}

    def register(self, key_name, component: tk.Widget) -> None:
        if isinstance(component, tk.Button):
            self.buttonMap[key_name] = component
        elif isinstance(component, tk.Entry):
            self.entryMap[key_name] = component
        elif isinstance(component, tk.Label):
            self.labelMap[key_name] = component

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

    def calculate(self, file_name):
        try:
            self._calculator.calculate(file_name)
        except Exception as err:
            self.render_error_msg(err)
