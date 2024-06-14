import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        
        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, height=100, bg='grey')
        display_frame.pack(expand=True, fill='both')
        
        # Entry box for the input
        input_box = tk.Entry(display_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bg='#eee', bd=0, justify='right')
        input_box.grid(row=0, column=0, ipadx=8, ipady=15, columnspan=4)

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(expand=True, fill='both')

        # Define the buttons
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        # Adding buttons to the buttons frame
        row_value = 0
        col_value = 0
        for button in buttons:
            if button == '=':
                button_widget = ttk.Button(buttons_frame, text=button, command=lambda: self.evaluate())
            elif button == 'C':
                button_widget = ttk.Button(buttons_frame, text=button, command=lambda: self.clear())
            else:
                button_widget = ttk.Button(buttons_frame, text=button, command=lambda button=button: self.add_to_expression(button))
                
            button_widget.grid(row=row_value, column=col_value, ipadx=15, ipady=15, sticky='nsew')

            col_value += 1
            if col_value > 3:
                col_value = 0
                row_value += 1

        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)

    def add_to_expression(self, value):
        self.expression += value
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
