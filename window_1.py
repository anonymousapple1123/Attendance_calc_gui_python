import tkinter as tk
import imp_msg_popup as popup_w
import ttkbootstrap as ttk
import calc_file as calc  # Assuming calc_file contains the required functions
from window_2_popup_button_1 import open_popup_button2, open_popup_button1, open_popup_button3  # Import the open_popup function

def create_gradient_background(canvas, width, height):
    # Create a super light gradient background from very light purple to white
    for i in range(height):
        r = int(255)  # Red stays at 255 for a light purple
        g = int(240 - (240 * (i / height)))  # Transition from light purple to white
        b = int(255)  # Blue stays at 255 for a light purple
        color = f'#{r:02x}{g:02x}{b:02x}'  # Create hex color
        canvas.create_line(0, i, width, i, fill=color)

def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Draw a rounded rectangle on the canvas."""
    canvas.create_arc(x1, y1, x1 + radius * 2, y1 + radius * 2, start=90, extent=90, **kwargs)  # Top-left
    canvas.create_arc(x2 - radius * 2, y1, x2, y1 + radius * 2, start=0, extent=90, **kwargs)  # Top-right
    canvas.create_arc(x1, y2 - radius * 2, x1 + radius * 2, y2, start=180, extent=90, **kwargs)  # Bottom-left
    canvas.create_arc(x2 - radius * 2, y2 - radius * 2, x2, y2, start=270, extent=90, **kwargs)  # Bottom-right
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)  # Middle
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)  # Middle

def main_window():
    # Function to calculate and display attendance
    def output_data_for_calculate_button():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = calc.percent_attendance(num1, num2)
            output_string.set(f'Attendance: {result:.2f} %')
        except ValueError:
            output_string.set('Please enter valid numbers.')

    # Function to open the popup window
    def output_data_for_button2():
        open_popup_button2(entry1, entry2, output_string)
    def output_data_for_button1():
        open_popup_button1(entry1, entry2, output_string)
    def output_data_for_button3():
        open_popup_button3(entry1, entry2, output_string)

    # Create the main window
    window = ttk.Window(themename='flatly')  # Change theme to 'flatly'
    window.title('Attendance Calculator')
    window.geometry('1480x850')

    # Create a canvas for the gradient background
    canvas = tk.Canvas(window, width=1480, height=850)
    canvas.pack(fill="both", expand=True)

    # Create the gradient background
    create_gradient_background(canvas, 1480, 850)

    # Title label
    title_label = ttk.Label(master=window, text='Calculate Attendance Percentage', font='Helvetica 24 bold', background='white')
    title_label.place(relx=0.5, rely=0.05, anchor='center')  # Adjusted position

    popup_w.show_popup()

    # Input frame
    input_frame = ttk.Frame(master=window, padding=20)
    input_frame.place(relx=0.5, rely=0.3, anchor='center')

    # First input field
    entry1 = ttk.Entry(master=input_frame, font='Helvetica 16', width=20)
    entry1.pack(pady=10, padx=10)

    # Second input field
    entry2 = ttk.Entry(master=input_frame, font='Helvetica 16', width=20)
    entry2.pack(pady=10, padx=10)

    # Button to perform calculation
    calculate_button = ttk.Button(master=input_frame, text='Calculate Attendance', command=output_data_for_calculate_button, bootstyle='primary', width=20)
    calculate_button.pack(pady=10)

    # Additional buttons
    button1 = ttk.Button(master=input_frame, text='Avoid Fine', command=output_data_for_button1, bootstyle='info', width=20)
    button1.pack(pady=5)

    button2 = ttk.Button(master=input_frame, text='Take Leave', command=output_data_for_button2, bootstyle='info', width=20)
    button2.pack(pady=5)

    button3 = ttk.Button(master=input_frame, text='Get Attendance', command=output_data_for_button3, bootstyle='info', width=20)
    button3.pack(pady=5)

    # Output label
    output_string = tk.StringVar()
    output_label = ttk.Label(master=window, text='Output', font='Helvetica 24', textvariable=output_string, background='white')
    output_label.place(relx=0.5, rely=0.8, anchor='center')

    # Run the main loop
    window.mainloop()

# Call the main_window function to run the application
if __name__ == "__main__":
    main_window()
