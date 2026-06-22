import tkinter as tk
from tkinter import messagebox

database = [ ]

class SimpleLostFoundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Lost & Found Portal")
        self.root.geometry("850x450") 
        
        title_label = tk.Label(root, text="Lost & Found Portal", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white", pady=10)
        title_label.pack(fill=tk.X)

        input_frame = tk.LabelFrame(root, text="Report an Item", font=("Arial", 11, "bold"), padx=10, pady=10)
        input_frame.place(x=15, y=70, width=250, height=350)

        tk.Label(input_frame, text="Report Type:").pack(anchor=tk.W, pady=2)
        self.type_var = tk.StringVar(value="Lost")
        tk.Radiobutton(input_frame, text="Lost", variable=self.type_var, value="Lost").pack(anchor=tk.W)
        tk.Radiobutton(input_frame, text="Found", variable=self.type_var, value="Found").pack(anchor=tk.W)

        tk.Label(input_frame, text="Item Name/Description:").pack(anchor=tk.W, pady=5)
        self.entry_item = tk.Entry(input_frame, width=25)
        self.entry_item.pack(fill=tk.X, pady=2)

        tk.Label(input_frame, text="Location:").pack(anchor=tk.W, pady=5)
        self.entry_loc = tk.Entry(input_frame, width=25)
        self.entry_loc.pack(fill=tk.X, pady=2)

        tk.Label(input_frame, text="Contact Info (Phone/Email):").pack(anchor=tk.W, pady=5)
        self.entry_contact = tk.Entry(input_frame, width=25)
        self.entry_contact.pack(fill=tk.X, pady=2)

        submit_btn = tk.Button(input_frame, text="Submit Report", bg="#2ecc71", fg="white", font=("Arial", 10, "bold"), command=self.add_item)
        submit_btn.pack(fill=tk.X, pady=15)

        display_frame = tk.LabelFrame(root, text="Recent Reports", font=("Arial", 11, "bold"), padx=10, pady=10)
        display_frame.place(x=280, y=70, width=550, height=350)

        self.item_listbox = tk.Listbox(display_frame, font=("Courier", 10), selectmode=tk.SINGLE)
        self.item_listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh_listbox()

    def add_item(self):
        item_type = self.type_var.get()
        item_name = self.entry_item.get().strip()
        location = self.entry_loc.get().strip()
        contact = self.entry_contact.get().strip()

        if not item_name or not location or not contact:
            messagebox.showerror("Error", "All fields are required!")
            return

        formatted_entry = f" [{item_type}]  {item_name}  |  Loc: {location}  |  Contact: {contact}"
        
        database.append(formatted_entry)

        messagebox.showinfo("Success", f"{item_type} item reported successfully!")
        self.clear_inputs()
        self.refresh_listbox()

    def refresh_listbox(self):
        self.item_listbox.delete(0, tk.END)
        
        for record in database:
            self.item_listbox.insert(tk.END, record)

    def clear_inputs(self):
        self.entry_item.delete(0, tk.END)
        self.entry_loc.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.type_var.set("Lost")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleLostFoundApp(root)
    root.mainloop()