import tkinter as tk

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

root = tk.Tk()
root.title("Список дел")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

btn_add = tk.Button(root, text="Добавить", command=add_task)
btn_add.pack(pady=5)

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=5)

btn_del = tk.Button(root, text="Удалить выбранное", command=delete_task)
btn_del.pack(pady=5)

root.mainloop()