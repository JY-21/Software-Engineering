import customtkinter as ctk

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Initialize the main application window
app = ctk.CTk()
app.title("Modern Calculator")
app.geometry("300x400")
app.resizable(False, False)

# Entry widget to display expressions and results
entry = ctk.CTkEntry(app, width=280, height=50, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks
def button_click(value)
    current = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(0, current + str(value))

# Function to clear the entry
def button_clear():
    entry.delete(0, ctk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, ctk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, ctk.END)
        entry.insert(0, "Error")

# Define button texts and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Create and place buttons on the grid
for btn in buttons:
    if len(btn) == 4:
        text, row, col, colspan = btn
        ctk.CTkButton(app, text=text, width=280, height=50, font=("Arial", 20),
                      command=lambda t=text: button_equal() if t == '=' else None).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)
    else:
        text, row, col = btn
        action = button_clear if text == 'C' else lambda t=text: button_click(t)
        ctk.CTkButton(app, text=text, width=60, height=50, font=("Arial", 20),
                      command=action).grid(row=row, column=col, padx=5, pady=5)

# Run the application
app.mainloop()
