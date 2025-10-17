import tkinter as tk

def say_hello():
    name = entry.get()
    if name.strip():
        greeting_label.config(text=f"Привет, {name}!")
    else:
        greeting_label.config(text="Введите имя!")

root = tk.Tk()
root.title("Простое приветствие")

tk.Label(root, text="Введите имя:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="Поздороваться", command=say_hello)
btn.pack(pady=5)

greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=5)

root.mainloop()
