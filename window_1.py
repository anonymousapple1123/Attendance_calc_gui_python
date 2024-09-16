import tkinter as tk
import ttkbootstrap as ttk
import calc_file as calc


def main_window():
    #name this function a generic name.
    def multiply():
        try:
            # Get the input from both entry fields
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            # Calculate the multiplication
            #Add here choice of inputs based on the button user have pressed.
            result = calc.percent_attendance(num1,num2)
            # Set the output string to the result
            output_string.set(f'Attendance : {result} %')
        except ValueError:
            output_string.set('Please enter valid numbers.')

    # Create the main window
    window = ttk.Window(themename='journal')
    window.title('Testing Window 0.01')
    window.geometry('700x450')

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

    # Button to perform multiplication
    button = ttk.Button(master=input_frame, text='Calculate', command=multiply)
    button.pack(pady=10)

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
