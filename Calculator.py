import tkinter

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Számológép")

        self.result_var = tkinter.StringVar()
        self.result_var.set("0")

        self.widgets()
    def widgets(self):
        result_entry = tkinter.Entry(self.master, textvariable=self.result_var, font=('Arial', 12), bd=10, insertwidth=4, width=13, justify='right')
        result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tkinter.Button(self.master, text=button, padx=13, pady=13, font=('Arial', 12), command=lambda b=button: self.buttons_work(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def buttons_work(self, value):
        if value == 'C':
            self.result_var.set("0")
        elif value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Hiba")
        else:
            current_value = self.result_var.get()
            if current_value == "0":
                current_value = ""
            current_value += value
            self.result_var.set(current_value)

def main():
    root = tkinter.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()