import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Food and Stationery Viewer")
        self.root.geometry("600x400")

        # Membuat tab untuk Food dan Stationery
        self.tab_control = ttk.Notebook(root)

        self.food_frame = ttk.Frame(self.tab_control)
        self.stationery_frame = ttk.Frame(self.tab_control)

        self.tab_control.add(self.food_frame, text='Food Menu')
        self.tab_control.add(self.stationery_frame, text='Stationery List')
        self.tab_control.pack(expand=1, fill="both")

        # Tabel untuk Food
        self.food_tree = ttk.Treeview(self.food_frame, columns=("Food", "Stand", "Price"), show='headings')
        self.food_tree.heading("Food", text="Food")
        self.food_tree.heading("Stand", text="Stand")
        self.food_tree.heading("Price", text="Price")
        self.food_tree.pack(fill=tk.BOTH, expand=True)

        # Tabel untuk Stationery
        self.stationery_tree = ttk.Treeview(self.stationery_frame, columns=("Item", "Price"), show='headings')
        self.stationery_tree.heading("Item", text="Item")
        self.stationery_tree.heading("Price", text="Price")
        self.stationery_tree.pack(fill=tk.BOTH, expand=True)

    def display_food_items(self, items):
        for item in items:
            self.food_tree.insert("", tk.END, values=item)

    def display_stationery_items(self, items):
        for item in items:
            self.stationery_tree.insert("", tk.END, values=item)

# Fungsi untuk menjalankan aplikasi dengan data yang didapat dari controller
def run_app(food_items, stationery_items):
    root = tk.Tk()
    view = View(root)

    # Tampilkan data yang diterima dari controller
    view.display_food_items(food_items)
    view.display_stationery_items(stationery_items)

    root.mainloop()
