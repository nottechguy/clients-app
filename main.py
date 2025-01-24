import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
import sqlite3

class ClientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Registration")

        # Initialize database
        self.conn = sqlite3.connect("clients.db")
        self.cursor = self.conn.cursor()
        self.create_table()

        # Configure responsive grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Labels and Entry fields
        ttk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = ttk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(root, text="Last Name:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.lastname_entry = ttk.Entry(root)
        self.lastname_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.email_entry = ttk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(root, text="Phone Number:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.phone_entry = ttk.Entry(root)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        # Treeview for displaying clients
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Last Name", "Email", "Phone"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Last Name", text="Last Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone", text="Phone Number")
        self.tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Make treeview scrollable
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=7, column=2, sticky="ns")

        # Configure resizing behavior
        self.root.rowconfigure(7, weight=1)

        # Load clients when the app starts
        self.view_clients()

        # Floating action button container
        self.fab_container = tk.Frame(self.root, bg="white", padx=10, pady=10)
        self.fab_container.grid(row=8, column=0, columnspan=2, sticky="se")

        # Floating action buttons
        self.add_fab_button("Register", self.register_client)
        self.add_fab_button("View Clients", self.view_clients)
        self.add_fab_button("Edit Selected", self.edit_client)
        self.add_fab_button("Delete Selected", self.delete_client)

    def add_fab_button(self, text, command):
        fab = tk.Button(self.fab_container, text=text, bg="#6200EE", fg="white", font=("Helvetica", 10, "bold"),
                        command=command, relief="raised", padx=10, pady=5, bd=2)
        fab.pack(side=tk.LEFT, padx=5)

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def register_client(self):
        name = self.name_entry.get().strip()
        lastname = self.lastname_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name or not lastname or not email or not phone:
            messagebox.showerror("Error", "All fields are required.")
            return

        self.cursor.execute("INSERT INTO clients (name, lastname, email, phone) VALUES (?, ?, ?, ?)",
                            (name, lastname, email, phone))
        self.conn.commit()
        messagebox.showinfo("Success", "Client registered successfully!")

        # Clear the fields after registration
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

        # Update the treeview
        self.view_clients()

    def view_clients(self):
        # Clear the treeview before displaying clients
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.cursor.execute("SELECT id, name, lastname, email, phone FROM clients")
        for client in self.cursor.fetchall():
            self.tree.insert("", tk.END, values=client)

    def edit_client(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No client selected.")
            return

        item = self.tree.item(selected_item)
        client_id = item["values"][0]
        name, lastname, email, phone = item["values"][1:]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)
        self.lastname_entry.delete(0, tk.END)
        self.lastname_entry.insert(0, lastname)
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, email)
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, phone)

        save_button = ttk.Button(self.root, text="Save Changes")

        def save_changes():
            new_name = self.name_entry.get().strip()
            new_lastname = self.lastname_entry.get().strip()
            new_email = self.email_entry.get().strip()
            new_phone = self.phone_entry.get().strip()

            if not new_name or not new_lastname or not new_email or not new_phone:
                messagebox.showerror("Error", "All fields are required.")
                return

            self.cursor.execute("UPDATE clients SET name = ?, lastname = ?, email = ?, phone = ? WHERE id = ?",
                                (new_name, new_lastname, new_email, new_phone, client_id))
            self.conn.commit()
            messagebox.showinfo("Success", "Client updated successfully!")
            self.view_clients()

            self.name_entry.delete(0, tk.END)
            self.lastname_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)

            save_button.destroy()

        save_button.config(command=save_changes)
        save_button.grid(row=4, column=2, padx=5, pady=5)

    def delete_client(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No client selected.")
            return

        item = self.tree.item(selected_item)
        client_id = item["values"][0]

        self.cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
        self.conn.commit()
        messagebox.showinfo("Success", "Client deleted successfully!")
        self.view_clients()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = ThemedTk(theme="arc")  # Using a material design-inspired theme
    app = ClientApp(root)
    root.mainloop()
