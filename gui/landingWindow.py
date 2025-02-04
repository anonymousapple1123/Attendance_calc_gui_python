
from PIL import Image, ImageTk  
import os
import tkinter as tk
import webbrowser
import ttkbootstrap as ttk
from gui import popupWindow

ICON_PATH = os.path.join(os.path.dirname(__file__), "../assets/app_icon.ico")


def only_integers(P):
    """
    Validation function: allows only integer input.
    """
    return P == "" or P.isdigit()

def open_donate_link(event):
    """Opens the donation URL in the default web browser."""
    webbrowser.open("https://www.linkedin.com/in/ayush-kumar-744056242/")

def show_owner_info(root):
    """
    Creates a small popup window (Toplevel) that displays the owner information
    and a donation link. Closes automatically after 8 seconds.
    """
    info_popup = ttk.Toplevel(root)
    info_popup.title("About")
    info_popup.geometry("450x200+400+50")
    info_popup.resizable(False, False)

    frame = ttk.Frame(info_popup, padding=10)
    frame.pack(expand=True, fill='both')

    owner_text = "Dude who built this -> Ayush"
    link_text = "Find me on : www.linkedin.com/"

    owner_label = ttk.Label(frame, text=owner_text, font="Helvetica 12")
    owner_label.pack(pady=(10, 5))

    link_label = ttk.Label(frame, text=link_text, font="Helvetica 12 underline", foreground="blue", cursor="hand2")
    link_label.pack(pady=(0, 10))
    link_label.bind("<Button-1>", open_donate_link)

    info_popup.after(8000, info_popup.destroy)

def main():
    window = ttk.Window(themename='flatly')
    window.title("Advanced Attendance Calculator")
    window.geometry("800x600")
    
    if os.path.exists(ICON_PATH):
        window.iconbitmap(ICON_PATH)
    # Show owner information popup on startup.
    show_owner_info(window)
    
    # Validation for integer inputs.
    vcmd = (window.register(only_integers), '%P')
    
    # Frame for the two main input fields.
    input_frame = ttk.Frame(window, padding=20)
    input_frame.pack(pady=30)
    
    label_absent = ttk.Label(input_frame, text="Enter the number of absent lectures:", font="Helvetica 14")
    label_absent.pack(pady=(0, 5))
    entry_absent = ttk.Entry(input_frame, font="Helvetica 16", width=30, validate="key", validatecommand=vcmd)
    entry_absent.pack(pady=(0, 20))
    
    label_total = ttk.Label(input_frame, text="Enter the total number of lectures:", font="Helvetica 14")
    label_total.pack(pady=(0, 5))
    entry_total = ttk.Entry(input_frame, font="Helvetica 16", width=30, validate="key", validatecommand=vcmd)
    entry_total.pack(pady=(0, 20))
    
    # Frame for the buttons.
    button_frame = ttk.Frame(window, padding=20)
    button_frame.pack(pady=20)
    
    common_bootstyle = "primary"
    btn_width = 20

    # When each button is pressed, the current absent and total values are read
    # (as strings) and passed (after conversion inside the popup functions) to the popup.
    btn1 = ttk.Button(button_frame, text="Calculate attendance", 
                      command=lambda: popupWindow.create_current_attendance_popup(entry_absent.get(), entry_total.get()),
                      bootstyle=common_bootstyle, width=btn_width)
    btn2 = ttk.Button(button_frame, text="avoid fine", 
                      command=lambda: popupWindow.create_avoid_fine_popup(entry_absent.get(), entry_total.get()),
                      bootstyle=common_bootstyle, width=btn_width)
    btn3 = ttk.Button(button_frame, text="Take Leave", 
                      command=lambda: popupWindow.create_take_leave_popup(entry_absent.get(), entry_total.get()),
                      bootstyle=common_bootstyle, width=btn_width)
    btn4 = ttk.Button(button_frame, text="Get attendance", 
                      command=lambda: popupWindow.create_get_attendance_popup(entry_absent.get(), entry_total.get()),
                      bootstyle=common_bootstyle, width=btn_width)
    
    btn1.grid(row=0, column=0, padx=10, pady=10)
    btn2.grid(row=0, column=1, padx=10, pady=10)
    btn3.grid(row=1, column=0, padx=10, pady=10)
    btn4.grid(row=1, column=1, padx=10, pady=10)
    
    # Fifth button (Settings) using a generic popup.
    btn_settings = ttk.Button(button_frame, text="Settings", 
                              command=popupWindow.create_generic_popup, 
                              bootstyle=common_bootstyle)
    btn_settings.grid(row=2, column=0, columnspan=2, pady=20)
    
    window.mainloop()

if __name__ == "__main__":
    main()
