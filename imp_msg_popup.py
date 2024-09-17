import tkinter as tk
def show_popup():
    # Create a new top-level window
    popup = tk.Toplevel()
    popup.title("Copyright Information")

    # Set the size of the popup window
    popup.geometry("580x450")  # Width x Height

    # Create a label with the copyright message
    copyright_message = "© 2023 Your Company Name\nAll rights reserved."
    label = tk.Label(popup, text=copyright_message, padx=20, pady=20)
    label.pack()

    # Create an OK button that closes the popup
    ok_button = tk.Button(popup, text="OK", command=popup.destroy, width=15, height=2)
    ok_button.pack(side=tk.BOTTOM, pady=10)

    # Center the popup window on the screen
    popup.update_idletasks()  # Update "requested size" from geometry manager
    width = popup.winfo_width()
    height = popup.winfo_height()
    x = (popup.winfo_screenwidth() // 2) - (width // 2)
    y = (popup.winfo_screenheight() // 2) - (height // 2)
    popup.geometry(f'{width}x{height}+{x}+{y}')  # Set the new geometry
