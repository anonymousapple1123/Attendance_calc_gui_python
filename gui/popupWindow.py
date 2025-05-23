import tkinter as tk
import ttkbootstrap as ttk
from logic import calculations, save_file_handler as save
INVALID_REQUEST=-1.01
NO_CHANGE=0


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
            current_attendance=calculations.percent_attendance(a,t)
            function_response = calculations.get_attendance(a, t, desired)

            if function_response == INVALID_REQUEST:
                result_label.config(text="Not possible.")
                
            elif function_response == NO_CHANGE:
                result_label.config(text="You have the desired attendance.")
            elif desired < current_attendance :
                result_label.config(text=f"Absent for {function_response} lectures OR {int(function_response/8)} days")
            elif desired > current_attendance :
                result_label.config(text=f"Present for {function_response} lectures OR {int(function_response/8)} days")
        except Exception as e:
            result_label.config(text="Error: Invalid input.")
    
    entry.bind("<Return>", process_input)
    entry.focus()


def create_settings_popup():
    """
    Creates a popup window for the Settings button.
    """
    popup = ttk.Toplevel()
    popup.title("Settings")
    popup.geometry("750x350")
    
    title_label = ttk.Label(popup, text="Settings", font="Helvetica 18 bold")
    title_label.pack(pady=10)

    # Input fields for settings
    theme_label = ttk.Label(popup, text="Lectures Per Day", font="Helvetica 10")
    theme_label.pack(pady=5)
    lectures_per_day = ttk.Entry(popup, font="Helvetica 16")
    lectures_per_day.pack(pady=5)

    font_size_label = ttk.Label(popup, text="Fine Every Percent", font="Helvetica 10")
    font_size_label.pack(pady=5)
    fine_per_percent = ttk.Entry(popup, font="Helvetica 16")
    fine_per_percent.pack(pady=5)

    # Load existing settings
    settings = save.load_settings()
    lectures_per_day.insert(0, settings.get('lectures_per_day', 8))
    fine_per_percent.insert(0, settings.get('fine_per_percent', 4000))

    result_label = ttk.Label(popup, text="", font="Helvetica 10")
    result_label.pack(pady=10)

    def save_and_update():
        """Save settings and update the display."""
        settings = {
            'lectures_per_day': lectures_per_day.get(),
            'fine_per_percent': fine_per_percent.get(),
        }
        save.save_settings(settings)
        result_label.config(text="Settings saved successfully!")
       # messagebox.showinfo("Settings", "Settings saved successfully!")

    save_button = ttk.Button(popup, text="Save Settings", command=save_and_update)
    save_button.pack(pady=10)

    # Display current settings
    current_values_label = ttk.Label(popup, text="", font="Helvetica 10")
    current_values_label.pack(pady=10)

    def update_display():
        current_values = f"Lecture count per day: {lectures_per_day.get()}\nFine every percent: {fine_per_percent.get()}"
        current_values_label.config(text=current_values)

    # Update display when input changes
    lectures_per_day.bind("<KeyRelease>", lambda event: update_display())
    fine_per_percent.bind("<KeyRelease>", lambda event: update_display())

    # Initial display of current values
    update_display()

