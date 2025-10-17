import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Ошибка")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=16, font=("Arial", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for btn_text in buttons:
    btn = tk.Button(root, text=btn_text, width=4, height=2, font=("Arial", 18),
                    command=lambda x=btn_text: on_click(x))
    btn.grid(row=row, column=col, padx=2, pady=2)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()