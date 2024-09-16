import tkinter as tk
import ttkbootstrap as ttk
import calc_file as calc  # Assuming calc_file contains the required functions
from window_2_popup_button_1 import open_popup  # Import the open_popup function

def main_window():
    # Function to calculate and display attendance
    def output_data_for_calulate_button():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = calc.percent_attendance(num1, num2)
            # Set the output string to the result
            output_string.set(f'Attendance: {result} %')
        except ValueError:
            output_string.set('Please enter valid numbers.')

    # Function to open the popup window
    def output_data_for_button2():
        open_popup(entry1, entry2, output_string)  # Open the popup and pass the necessary references

    # Create the main window
    window = ttk.Window(themename='journal')
    window.title('Testing Window 0.01')
    window.geometry('900x650')

    # Title label
    title_label = ttk.Label(master=window, text='Calculate Percentage', font='Calibri 24 bold')
    title_label.pack()

    # Input frame
    input_frame = ttk.Frame(master=window)

    # First input field
    entry1 = ttk.Entry(master=input_frame)
    entry1.pack(pady=5)

    # Second input field
    entry2 = ttk.Entry(master=input_frame)
    entry2.pack(pady=5)

    # Button to perform calculation
    calculate_button = ttk.Button(master=input_frame, text='Calculate', command=output_data_for_calulate_button)
    calculate_button.pack(pady=10)

    # Additional buttons
    button1 = ttk.Button(master=input_frame, text='Button 1')
    button1.pack(pady=5)

    button2 = ttk.Button(master=input_frame, text='Open Popup', command=output_data_for_button2)  # Link to open the popup
    button2.pack(pady=5)

    button3 = ttk.Button(master=input_frame, text='Button 3')
    button3.pack(pady=5)

    input_frame.pack(pady=50)

    # Output label
    output_string = tk.StringVar()
    output_label = ttk.Label(master=window, text='Output',
                             font='Calibri 24',
                             textvariable=output_string)
    output_label.pack(pady=15)

    # Run the main loop
    window.mainloop()

# Call the main_window function to run the application
if __name__ == "__main__":
    main_window()
