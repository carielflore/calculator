import tkinter as tk

from calculator.gui import CalculatorGUI


def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
