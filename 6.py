import tkinter as tk
import random

def check_guess():
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Введите число!")
        return

    global attempts
    attempts += 1

    if guess < number:
        result_label.config(text="Больше")
    elif guess > number:
        result_label.config(text="Меньше")
    else:
        result_label.config(text=f"Угадано за {attempts} попыток!")
        btn_check.config(state="disabled")

    attempts_label.config(text=f"Попыток: {attempts}")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Игра 'Угадай число'")

number = random.randint(1, 100)
attempts = 0

tk.Label(root, text="Угадайте число от 1 до 100").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_check = tk.Button(root, text="Проверить", command=check_guess)
btn_check.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

attempts_label = tk.Label(root, text="Попыток: 0")
attempts_label.pack(pady=5)

root.mainloop()