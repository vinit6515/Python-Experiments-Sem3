import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to create the user_info table
def create_user_info_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def create_new_user_window():
    new_user_window = tk.Toplevel(root)
    new_user_window.title("New User Registration")

    # Create labels and entry widgets for new user details
    tk.Label(new_user_window, text="New Username:").pack()
    new_username_entry = tk.Entry(new_user_window)
    new_username_entry.pack()

    tk.Label(new_user_window, text="New Password:").pack()
    new_password_entry = tk.Entry(new_user_window, show="*")
    new_password_entry.pack()

    def save_new_user():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        # Save new user to the database
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user_info (username, password) VALUES (?, ?)", (new_username, new_password))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "New user created successfully!")
        new_user_window.destroy()

    tk.Button(new_user_window, text="Save", command=save_new_user).pack()

# Call the function to create the user_info table before running the application
create_user_info_table()

# Main application window
root = tk.Tk()
root.title("Login System")

# Create labels and entry widgets for login details
tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

#create login button function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Check if user exists in the database
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_info WHERE username = ? AND password = ?", (username, password))
    user_data = cursor.fetchone()
    conn.close()

    if user_data:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Login button
tk.Button(root, text="Login", command=login).pack()

# New user button
tk.Button(root, text="New User", command=create_new_user_window).pack()

root.mainloop()


