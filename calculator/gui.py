import tkinter as tk
from tkinter import ttk

from calculator.core import Calculator


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.calc = Calculator()
        self.current_input = ""
        self.stored_value = None
        self.operation = None

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 24), justify="right", bd=10)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
            ("%", 5, 0),
            ("^", 5, 1),
            ("√", 5, 2),
            ("C", 5, 3),
            ("sin", 6, 0),
            ("cos", 6, 1),
            ("floor", 6, 2),
            ("ceil", 6, 3),
        ]

        for text, row, col in buttons:
            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18),
                command=lambda t=text: self.on_button_click(t),
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char.isdigit() or char == ".":
            self.current_input += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_input)

        elif char == "C":
            self.current_input = ""
            self.stored_value = None
            self.operation = None
            self.display.delete(0, tk.END)

        elif char in ["+", "-", "*", "/", "%", "^"]:
            if self.current_input:
                self.stored_value = float(self.current_input)
                self.operation = char
                self.current_input = ""

        elif char == "=":
            if self.stored_value is not None and self.operation and self.current_input:
                try:
                    current = float(self.current_input)
                    if self.operation == "+":
                        result = self.calc.add(self.stored_value, current)
                    elif self.operation == "-":
                        result = self.calc.subtract(self.stored_value, current)
                    elif self.operation == "*":
                        result = self.calc.multiply(self.stored_value, current)
                    elif self.operation == "/":
                        result = self.calc.divide(self.stored_value, current)
                    elif self.operation == "%":
                        result = self.calc.modulo(self.stored_value, current)
                    elif self.operation == "^":
                        result = self.calc.power(self.stored_value, current)

                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                    self.current_input = str(result)
                    self.stored_value = None
                    self.operation = None
                except ValueError as e:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    self.current_input = ""

        elif char == "√":
            if self.current_input:
                try:
                    result = self.calc.sqrt(float(self.current_input))
                    self.display.delete(0, tk.END)
                    self.display.insert(0, str(result))
                    self.current_input = str(result)
                except ValueError as e:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    self.current_input = ""

        elif char == "sin":
            if self.current_input:
                result = self.calc.sin(float(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)

        elif char == "cos":
            if self.current_input:
                result = self.calc.cos(float(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)

        elif char == "floor":
            if self.current_input:
                result = self.calc.floor(float(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)

        elif char == "ceil":
            if self.current_input:
                result = self.calc.ceil(float(self.current_input))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)
