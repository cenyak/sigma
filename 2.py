import tkinter as tk

def change_theme():
    theme = theme_var.get()
    if theme == "light":
        root.config(bg="white")
        label.config(bg="white", fg="black")
    else:
        root.config(bg="black")
        label.config(bg="black", fg="white")

root = tk.Tk()
root.title("Переключатель тем")

theme_var = tk.StringVar(value="light")

radio_light = tk.Radiobutton(root, text="Светлая тема", variable=theme_var, value="light", command=change_theme)
radio_dark = tk.Radiobutton(root, text="Темная тема", variable=theme_var, value="dark", command=change_theme)
radio_light.pack(anchor="w")
radio_dark.pack(anchor="w")

label = tk.Label(root, text="Текст для демонстрации темы", bg="white", fg="black", font=("Arial", 14))
label.pack(pady=20, fill="x")

root.mainloop()