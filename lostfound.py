import tkinter as tk
from tkinter import messagebox
from datetime import datetime

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

        filter_frame = tk.LabelFrame(root, text="Search & Date Filters", font=("Arial", 11, "bold"), padx=10, pady=5)
        filter_frame.place(x=280, y=70, width=550, height=95)

        # Search Bar Entry
        tk.Label(filter_frame, text="Search Item:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.entry_search = tk.Entry(filter_frame, width=14)
        self.entry_search.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(filter_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.entry_date_filter = tk.Entry(filter_frame, width=12)
        self.entry_date_filter.grid(row=0, column=3, padx=5, pady=5)

        btn_filter = tk.Button(filter_frame, text="Filter", bg="#3498db", fg="white", font=("Arial", 9, "bold"), command=self.refresh_listbox)
        btn_filter.grid(row=0, column=4, padx=5, pady=5)

        btn_reset = tk.Button(filter_frame, text="Reset", bg="#95a5a6", fg="white", font=("Arial", 9, "bold"), command=self.reset_filters)
        btn_reset.grid(row=0, column=5, padx=5, pady=5)

        display_frame = tk.LabelFrame(root, text="Recent Reports", font=("Arial", 11, "bold"), padx=10, pady=10)
        display_frame.place(x=280, y=180, width=550, height=310)

        self.item_listbox = tk.Listbox(display_frame, font=("Courier", 10), selectmode=tk.SINGLE)
        self.item_listbox.pack(fill=tk.BOTH, expand=True)

        self.refresh_listbox()

    def check_for_matches(self, new_type, new_item):
        look_for_type = "Found" if new_type == "Lost" else "Lost"
        matches_found = []

        for record in database:
            # Check if the string contains the opposing type AND the item keyword
            if f"[{look_for_type}]" in record and new_item.lower() in record.lower():
                matches_found.append(f"• {record.strip()}")

        if matches_found:
            alert_message = f"🚨 POTENTIAL MATCH ALERT! 🚨\n\nYou reported a '{new_type}' item: {new_item}.\n\n"
            alert_message += "We found these matches in the system:\n" + "\n".join(matches_found)
            messagebox.showinfo("System Match Found", alert_message)

    def add_item(self):
        item_type = self.type_var.get()
        item_name = self.entry_item.get().strip()
        location = self.entry_loc.get().strip()
        contact = self.entry_contact.get().strip()

        current_date = datetime.now().strftime("%Y-%m-%d")

        if not item_name or not location or not contact:
            messagebox.showerror("Error", "All fields are required!")
            return

        formatted_entry = f" [{current_date}] [{item_type}]  {item_name}  |  Loc: {location}  |  Contact: {contact}"
        database.append(formatted_entry)

        messagebox.showinfo("Success", f"{item_type} item reported successfully!")

        self.check_for_matches(item_type, item_name)
        self.clear_inputs()
        self.refresh_listbox()

    def refresh_listbox(self):
        self.item_listbox.delete(0, tk.END)
        
        search_query = self.entry_search.get().strip().lower()
        date_query = self.entry_date_filter.get().strip()

        for record in database:
            if search_query and search_query not in record.lower():
                continue
            if date_query and f"[{date_query}]" not in record:
                continue

            self.item_listbox.insert(tk.END, record)

    def reset_filters(self):
        self.entry_search.delete(0, tk.END)
        self.entry_date_filter.delete(0, tk.END)
        self.refresh_listbox()

    def clear_inputs(self):
        self.entry_item.delete(0, tk.END)
        self.entry_loc.delete(0, tk.END)
        self.entry_contact.delete(0, tk.END)
        self.type_var.set("Lost")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleLostFoundApp(root)
    root.mainloop()