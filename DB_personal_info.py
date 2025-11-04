import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database setup
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            salary FLOAT,
            address TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    messagebox.showinfo("Success", "Table created successfully!")

def insert_user():
    name = name_entry.get()
    age = age_entry.get()
    salary = salary_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()

    if not name or not age or not salary or not address or not phone:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        cursor.execute(
            "INSERT INTO users (name, age, salary, address, phone) VALUES (?, ?, ?, ?, ?)", 
            (name, int(age), float(salary), address, phone)
        )
        conn.commit()
        messagebox.showinfo("Success", "Record inserted successfully!")
        clear_entries()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def read_users():
    output_text.delete("1.0", tk.END)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    for row in rows:
        output_text.insert(tk.END, f"--------------------------------------------------------------------------\n{row}\n")

# ---------------- UPDATE HANDLING ----------------
def show_update_fields():
    hide_all_extra()
    update_frame.grid(row=9, column=0, columnspan=6, pady=10)

def update_user():
    field = field_entry.get()
    new_value = new_value_entry.get()
    user_id = user_id_entry.get()

    if not field or not new_value or not user_id:
        messagebox.showerror("Error", "All fields are required.")
        return

    if field not in {"name", "age", "salary", "address", "phone"}:
        messagebox.showerror("Error", "Invalid field name!")
        return

    confirm = messagebox.askyesno("Confirm Update", f"Update user {user_id}'s {field} to '{new_value}'?")
    if not confirm:
        return

    try:
        cursor.execute(f"UPDATE users SET {field} = ? WHERE id = ?", (new_value, user_id))
        conn.commit()
        messagebox.showinfo("Success", "Record updated successfully!")
        hide_all_extra()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- DELETE HANDLING ----------------
def show_delete_field():
    hide_all_extra()
    delete_frame.grid(row=9, column=0, columnspan=6, pady=10)

def delete_user():
    user_id = del_user_id_entry.get()
    if not user_id:
        messagebox.showerror("Error", "Enter User ID to delete.")
        return

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete user {user_id}?")
    if not confirm:
        return

    try:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        hide_all_extra()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_entries():
    for entry in (name_entry, age_entry, salary_entry, address_entry, phone_entry,
                  field_entry, new_value_entry, user_id_entry, del_user_id_entry):
        entry.delete(0, tk.END)

def hide_all_extra():
    update_frame.grid_remove()
    delete_frame.grid_remove()

# GUI setup
root = tk.Tk()
root.title("SQLite User Manager")

entry_width = 30
button_width = 15
button_height = 2

# Input fields
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root, width=entry_width)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
age_entry = tk.Entry(root, width=entry_width)
age_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Salary:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
salary_entry = tk.Entry(root, width=entry_width)
salary_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
address_entry = tk.Entry(root, width=entry_width)
address_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
phone_entry = tk.Entry(root, width=entry_width)
phone_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons row
tk.Button(root, text="Create Table", command=create_table, width=button_width, height=button_height).grid(row=5, column=0, padx=5, pady=5)
tk.Button(root, text="Insert", command=insert_user, width=button_width, height=button_height).grid(row=5, column=1, padx=5, pady=5)
tk.Button(root, text="Read", command=read_users, width=button_width, height=button_height).grid(row=5, column=2, padx=5, pady=5)
tk.Button(root, text="Update", command=show_update_fields, width=button_width, height=button_height).grid(row=5, column=3, padx=5, pady=5)
tk.Button(root, text="Delete", command=show_delete_field, width=button_width, height=button_height).grid(row=5, column=4, padx=5, pady=5)
tk.Button(root, text="Clear", command=clear_entries, width=button_width, height=button_height).grid(row=5, column=5, padx=5, pady=5)

# Extra Frames (Hidden)
update_frame = tk.Frame(root)
tk.Label(update_frame, text="Field:").grid(row=0, column=0, padx=5, pady=5)
field_entry = tk.Entry(update_frame, width=20)
field_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(update_frame, text="New Value:").grid(row=0, column=2, padx=5, pady=5)
new_value_entry = tk.Entry(update_frame, width=20)
new_value_entry.grid(row=0, column=3, padx=5, pady=5)
tk.Label(update_frame, text="User ID:").grid(row=0, column=4, padx=5, pady=5)
user_id_entry = tk.Entry(update_frame, width=10)
user_id_entry.grid(row=0, column=5, padx=5, pady=5)
tk.Button(update_frame, text="Confirm Update", command=update_user, bg="orange").grid(row=0, column=6, padx=5, pady=5)

delete_frame = tk.Frame(root)
tk.Label(delete_frame, text="User ID:").grid(row=0, column=0, padx=5, pady=5)
del_user_id_entry = tk.Entry(delete_frame, width=20)
del_user_id_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(delete_frame, text="Confirm Delete", command=delete_user, bg="red", fg="white").grid(row=0, column=2, padx=5, pady=5)

hide_all_extra()

# Output text area
output_text = tk.Text(root, height=10, width=100)
output_text.grid(row=10, column=0, columnspan=6, padx=10, pady=10)

root.mainloop()
conn.close()

