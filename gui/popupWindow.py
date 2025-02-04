import tkinter as tk
import ttkbootstrap as ttk
from logic import calculations

def only_integers(P):
    """Validation function to allow only integers."""
    return P == "" or P.isdigit()

def create_current_attendance_popup(absent, total):
    """
    Creates a popup window with the title "Current Attendance" that calculates
    the attendance percentage using calculations.percent_attendance and displays:
      "Your attendance is: <result>%"
    """
    popup = ttk.Toplevel()
    popup.title("Current Attendance")
    popup.geometry("400x200")
    
    try:
        a = float(absent)
        t = float(total)
        percent = calculations.percent_attendance(a, t)
        message = f"Your attendance is: {percent:.2f}%"
    except Exception as e:
        message = "Error: Invalid input values."
    
    message_label = ttk.Label(popup, text=message, font="Helvetica 16")
    message_label.pack(expand=True, pady=40)

def create_avoid_fine_popup(absent, total):
    """
    Creates a popup window for the "avoid fine" button.
    Title: "Input Leave"
    Displays grey helper text and an integer-only input field.
    When Enter is pressed, calculates the lectures to be present using calculations.avoid_fine.
    """
    popup = ttk.Toplevel()
    popup.title("Input Leave")
    popup.geometry("1000x500")
    
    description = "Provide the number of days you want to take the leave and avoid fine as well."
    desc_label = ttk.Label(popup, text=description, font="Helvetica 14", foreground="grey")
    desc_label.pack(pady=20)
    
    vcmd = (popup.register(only_integers), '%P')
    entry = ttk.Entry(popup, font="Helvetica 16", width=25, validate="key", validatecommand=vcmd)
    entry.pack(pady=10)
    
    result_label = ttk.Label(popup, text="", font="Helvetica 14", foreground="grey")
    result_label.pack(pady=10)
    
    def process_input(event):
        try:
            leave_days = int(entry.get())
            a = float(absent)
            t = float(total)
            result = calculations.avoid_fine(a, t, leave_days)
            result_label.config(text=f"Present for : {result} lectures or {int(result/8)} Days.")
        except Exception as e:
            result_label.config(text="Error: Invalid input.")
    
    entry.bind("<Return>", process_input)
    entry.focus()

def create_take_leave_popup(absent, total):
    """
    Creates a popup window for the "Take Leave" button.
    Title: "Input Leave"
    Displays grey helper text and an integer-only input field.
    When Enter is pressed, calculates the attendance after leave using calculations.need_leave.
    """
    popup = ttk.Toplevel()
    popup.title("Input Leave")
    popup.geometry("800x400")
    
    description = "Provide the number of days you want to take leave"
    desc_label = ttk.Label(popup, text=description, font="Helvetica 14", foreground="grey")
    desc_label.pack(pady=20)
    
    vcmd = (popup.register(only_integers), '%P')
    entry = ttk.Entry(popup, font="Helvetica 16", width=25, validate="key", validatecommand=vcmd)
    entry.pack(pady=10)
    
    result_label = ttk.Label(popup, text="", font="Helvetica 14", foreground="grey")
    result_label.pack(pady=10)
    
    def process_input(event): 
        try:
            days = int(entry.get())
            a = float(absent)
            t = float(total)
            result = calculations.need_leave(a, t, days)
            result_label.config(text=f"Attendance after your leave: {result:.2f}%")
        except Exception as e:
            result_label.config(text="Error: Invalid input.")
    
    entry.bind("<Return>", process_input)
    entry.focus()

def create_get_attendance_popup(absent, total):
    """
    Creates a popup window for the "Get attendance" button.
    Title: "Get attendance"
    Displays grey helper text and an integer-only input field.
    When Enter is pressed, calculates the lectures needed (or surplus) to reach the desired attendance using calculations.get_attendance.
    """
    popup = ttk.Toplevel()
    popup.title("Get attendance")
    popup.geometry("600x300")
    
    description = "Input the attendance percent you want to reach"
    desc_label = ttk.Label(popup, text=description, font="Helvetica 14", foreground="grey")
    desc_label.pack(pady=20)
    
    vcmd = (popup.register(only_integers), '%P')
    entry = ttk.Entry(popup, font="Helvetica 16", width=25, validate="key", validatecommand=vcmd)
    entry.pack(pady=10)
    
    result_label = ttk.Label(popup, text="", font="Helvetica 14", foreground="grey")
    result_label.pack(pady=10)
    
    def process_input(event):
        try:
            desired = int(entry.get())
            a = float(absent)
            t = float(total)
            current_attendance=calculations.get_attendance(a,t)
            result = calculations.get_attendance(a, t, desired)
            if result==100 and current_attendance!=100:
                result_label.config(text="Not possible.")
            else :
                result_label.config(text=f"Present for {result} lectures OR {int(result/8)} days")
        except Exception as e:
            result_label.config(text="Error: Invalid input.")
    
    entry.bind("<Return>", process_input)
    entry.focus()

def create_generic_popup():
    """
    Creates a generic popup window (for the Settings button, for example).
    """
    popup = ttk.Toplevel()
    popup.title("Popup Window")
    popup.geometry("400x300")
    
    title_label = ttk.Label(popup, text="Popup Window", font="Helvetica 18 bold")
    title_label.pack(pady=20)
    
    entry = ttk.Entry(popup, font="Helvetica 16", width=25)
    entry.pack(pady=10)
    
    result_label = ttk.Label(popup, text="Result:", font="Helvetica 16")
    result_label.pack(pady=10)
    
    def process_input(event):
        user_input = entry.get()
        try:
            value = float(user_input)
            result = value * 2  # Example calculation.
            result_label.config(text=f"Result: {result}")
        except ValueError:
            result_label.config(text="Invalid input. Please enter a number.")
    
    entry.bind("<Return>", process_input)
    entry.focus()
