import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if filepath:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{e}")

def save_as():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")])
    if filepath:
        try:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(text.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{e}")

root = tk.Tk()
root.title("Простой текстовый редактор")
root.geometry("600x400")

text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Открыть", command=open_file)
filemenu.add_command(label="Сохранить как", command=save_as)
menubar.add_cascade(label="Файл", menu=filemenu)

root.config(menu=menubar)
root.mainloop()