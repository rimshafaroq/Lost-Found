import tkinter as tk
from tkinter import messagebox
from datetime import datetime

database = [ ]

CATEGORIES = ["All Categories", "Electronics", "Documents/ID", "Books/Stationery", "Keys/Wallets", "Bags/Clothing", "Others"]
REPORT_CATEGORIES = CATEGORIES[1:] 

class SimpleLostFoundApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Lost & Found Portal")
        self.root.geometry("860x500") 
        self.root.configure(bg="#f8f9fa")
    
        title_label = tk.Label(root, text="Lost & Found Portal", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white", pady=12)
        title_label.pack(fill=tk.X)

        input_frame = tk.LabelFrame(root, text="Report an Item", font=("Arial", 11, "bold"), bg="#ffffff", fg="#2c3e50", padx=12, pady=8, bd=2)
        input_frame.place(x=15, y=75, width=260, height=400)

        tk.Label(input_frame, text="Report Type:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").pack(anchor=tk.W, pady=2)
        self.type_var = tk.StringVar(value="Lost")
    
        tk.Radiobutton(input_frame, text="Lost Item", font=("Arial", 9), bg="#ffffff", fg="#c0392b", activebackground="#ffffff", variable=self.type_var, value="Lost").pack(anchor=tk.W, padx=5)
        tk.Radiobutton(input_frame, text="Found Item", font=("Arial", 9), bg="#ffffff", fg="#27ae60", activebackground="#ffffff", variable=self.type_var, value="Found").pack(anchor=tk.W, padx=5)

        tk.Label(input_frame, text="Category:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").pack(anchor=tk.W, pady=4)
        self.category_var = tk.StringVar(value=REPORT_CATEGORIES[0])
        self.category_menu = tk.OptionMenu(input_frame, self.category_var, *REPORT_CATEGORIES)
        self.category_menu.configure(bg="#f1f2f6", activebackground="#e4e7eb", font=("Arial", 9), bd=1)
        self.category_menu.pack(fill=tk.X, pady=2)

        tk.Label(input_frame, text="Item Name/Description:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").pack(anchor=tk.W, pady=4)
        self.entry_item = tk.Entry(input_frame, width=25, bg="#f1f2f6", bd=1, font=("Arial", 10))
        self.entry_item.pack(fill=tk.X, pady=2, ipady=3)

        tk.Label(input_frame, text="Location:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").pack(anchor=tk.W, pady=4)
        self.entry_loc = tk.Entry(input_frame, width=25, bg="#f1f2f6", bd=1, font=("Arial", 10))
        self.entry_loc.pack(fill=tk.X, pady=2, ipady=3)

        tk.Label(input_frame, text="Contact Info (Phone/Email):", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").pack(anchor=tk.W, pady=4)
        self.entry_contact = tk.Entry(input_frame, width=25, bg="#f1f2f6", bd=1, font=("Arial", 10))
        self.entry_contact.pack(fill=tk.X, pady=2, ipady=3)

        submit_btn = tk.Button(input_frame, text="Submit Report", bg="#2ecc71", fg="white", activebackground="#27ae60", activeforeground="white", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.add_item)
        submit_btn.pack(fill=tk.X, pady=12, ipady=4)

        filter_frame = tk.LabelFrame(root, text="Search & Filters", font=("Arial", 11, "bold"), bg="#ffffff", fg="#2c3e50", padx=12, pady=5, bd=2)
        filter_frame.place(x=295, y=75, width=545, height=115)

        tk.Label(filter_frame, text="Search:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").grid(row=0, column=0, padx=2, pady=5, sticky=tk.W)
        self.entry_search = tk.Entry(filter_frame, width=12, bg="#f1f2f6", bd=1, font=("Arial", 10))
        self.entry_search.grid(row=0, column=1, padx=4, pady=5, ipady=2)

        tk.Label(filter_frame, text="Date:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").grid(row=0, column=2, padx=2, pady=5, sticky=tk.W)
        self.entry_date_filter = tk.Entry(filter_frame, width=11, bg="#f1f2f6", bd=1, font=("Arial", 10))
        self.entry_date_filter.grid(row=0, column=3, padx=4, pady=5, ipady=2)

        tk.Label(filter_frame, text="Category:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#34495e").grid(row=0, column=4, padx=2, pady=5, sticky=tk.W)
        self.filter_cat_var = tk.StringVar(value="All Categories")
        self.filter_cat_menu = tk.OptionMenu(filter_frame, self.filter_cat_var, *CATEGORIES)
        self.filter_cat_menu.configure(bg="#f1f2f6", activebackground="#e4e7eb", font=("Arial", 9), bd=1)
        self.filter_cat_menu.grid(row=0, column=5, padx=4, pady=5)

        btn_filter = tk.Button(filter_frame, text="Apply Filter", bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white", font=("Arial", 9, "bold"), bd=0, padx=10, cursor="hand2", command=self.refresh_listbox)
        btn_filter.grid(row=1, column=4, padx=5, pady=2, sticky=tk.E, ipady=2)

        btn_reset = tk.Button(filter_frame, text="Reset", bg="#95a5a6", fg="white", activebackground="#7f8c8d", activeforeground="white", font=("Arial", 9, "bold"), bd=0, padx=12, cursor="hand2", command=self.reset_filters)
        btn_reset.grid(row=1, column=5, padx=5, pady=2, sticky=tk.W, ipady=2)

        display_frame = tk.LabelFrame(root, text="Active Database Records", font=("Arial", 11, "bold"), bg="#ffffff", fg="#2c3e50", padx=12, pady=10, bd=2)
        display_frame.place(x=295, y=205, width=545, height=270)

        self.item_listbox = tk.Listbox(display_frame, font=("Courier", 9, "bold"), bg="#2c3e50", fg="#ecf0f1", selectbackground="#34495e", selectforeground="#2ecc71", bd=0, highlightthickness=0)
        self.item_listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh_listbox()

    def check_and_resolve_matches(self, new_type, new_item, new_location):
        look_for_type = "Found" if new_type == "Lost" else "Lost"
        matched_record = None
        location_check = f"Loc: {new_location}"

        for record in database:
            if (f"[{look_for_type}]" in record and 
                new_item.lower() in record.lower() and 
                location_check.lower() in record.lower()):
                
                matched_record = record
                break

        if matched_record:
            database.remove(matched_record)
            
            alert_message = f"🎉 LOCATION MATCH RESOLUTION SUCCESS! 🎉\n\n" \
                            f"You reported a '{new_type}' entry for '{new_item}' at '{new_location}'.\n\n" \
                            f"The system cleared this corresponding item from active display:\n" \
                            f"{matched_record.strip()}"
            messagebox.showinfo("System Strict Auto-Resolution", alert_message)
            return True 
            
        return False 

    def add_item(self):
        item_type = self.type_var.get()
        category = self.category_var.get()
        item_name = self.entry_item.get().strip()
        location = self.entry_loc.get().strip()
        contact = self.entry_contact.get().strip()

        current_date = datetime.now().strftime("%Y-%m-%d")

        if not item_name or not location or not contact:
            messagebox.showerror("Error", "All fields are required!")
            return

        is_matched = self.check_and_resolve_matches(item_type, item_name, location)

        if not is_matched:
            formatted_entry = f" [{current_date}] [{item_type}] [{category}] {item_name} | Loc: {location} | Contact: {contact}"
            database.append(formatted_entry)
            messagebox.showinfo("Success", f"{item_type} item reported successfully!")

        self.clear_inputs()
        self.refresh_listbox()

    def refresh_listbox(self):
        self.item_listbox.delete(0, tk.END)
        
        search_query = self.entry_search.get().strip().lower()
        date_query = self.entry_date_filter.get().strip()
        category_query = self.filter_cat_var.get()

        for record in database:
            if search_query and search_query not in record.lower():
                continue
            if date_query and f"[{date_query}]" not in record:
                continue
            if category_query != "All Categories" and f"[{category_query}]" not in record:
                continue

            self.item_listbox.insert(tk.END, record)

    def reset_filters(self):
        self.entry_search.delete(0, tk.END)
        self.entry_date_filter.delete(0, tk.END)
        self.filter_cat_var.set("All Categories")
        self.refresh_listbox()

    def clear_inputs(self):
        self.entry_item.delete(0, tk.END)
        self.entry_loc.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.type_var.set("Lost")
        self.category_var.set(REPORT_CATEGORIES[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleLostFoundApp(root)
    root.mainloop()