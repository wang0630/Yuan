import tkinter as tk
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
            elm = tk.Button(**config)
        elif component_type == ComponentType.entry:
            m = self.entryMap
            elm = tk.Entry(**config)
        else:
            raise Exception("component_type provided not available")
        # if key_name in m:
        #     return m[key_name]
        m[key_name] = elm
        return elm

    def get_component(self, component_type, key_name):
        if component_type == ComponentType.label:
            m = self.labelMap
        elif component_type == ComponentType.button:
            m = self.buttonMap
        elif component_type == ComponentType.entry:
            m = self.entryMap
        else:
            raise Exception("component_type provided not available")
        if key_name in m:
            return m[key_name]
        else:
            return None

    def render_error_msg(self, err: Exception):
        # Error msg
        error_msg_label = self.register(ComponentType.label, "error_msg", {
            "master": self,
            "bg": "#5DBB63",
            "foreground": "red",
        })
        error_msg_label["text"] = str(err)
        error_msg_label.grid(row=6, columnspan=2, pady=5)

    def dismiss_error(self):
        error_msg_label = self.get_component(ComponentType.label, "error_msg")
        if not error_msg_label:
            return
        if error_msg_label.winfo_ismapped():
            error_msg_label.grid_remove()

    def set_file(self, file_name):
        if not file_name:
            return
        self._file_name = file_name
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
        file_name_label["text"] = file_name
        file_name_label.grid(row=0, column=3, pady=5, padx=5)

    def calculate(self):
        try:
            self.dismiss_error()
            if self._file_name is None:
                raise Exception("Must provide file name before calculation.")
            entry = self.get_component(ComponentType.entry, "vd_constraints")
            constraints = []
            constraints_string = entry.get()
            if constraints_string:
                constraints = constraints_string.split(",")
                for (index, c) in enumerate(constraints):
                    constraints[index] = float(c)
            result = self._calculator.calculate(self._file_name, constraints)
            print(result)
            x1_label = self.register(ComponentType.label, "x1", self.create_config(result["x1"]))
            y1_label = self.register(ComponentType.label, "y1", self.create_config(result["y1"]))
            x2_label = self.register(ComponentType.label, "x2", self.create_config(result["x2"]))
            y2_label = self.register(ComponentType.label, "y2", self.create_config(result["y2"]))
            x_intercept_label = self.register(ComponentType.label, "x_intercept", self.create_config(result["x_intercept"]))

            x_intercept_label.grid(row=3, columnspan=1, pady=5)
            x1_label.grid(row=4, column=0, pady=5)
            y1_label.grid(row=4, column=1, pady=5)
            x2_label.grid(row=5, column=0, pady=5)
            y2_label.grid(row=5, column=1, pady=5)
        except Exception as err:
            self.render_error_msg(err)

    def create_config(self, text):
        return {
                "master": self,
                "text": text,
                "fg": "black",
            }

