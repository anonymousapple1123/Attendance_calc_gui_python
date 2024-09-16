#file has been added and works as intended.
import ttkbootstrap as ttk

def open_popup(entry1, entry2, output_string):
    # Create a new window
    popup_window = ttk.Window(themename='journal')
    popup_window.title('Additional Input')
    popup_window.geometry('300x200')

    # Label for the popup
    label = ttk.Label(master=popup_window, text='Enter additional input:', font='Calibri 14')
    label.pack(pady=10)

    # Entry field for additional input
    additional_input = ttk.Entry(master=popup_window)
    additional_input.pack(pady=5)

    # Function to handle input and perform multiplication
    def handle_input(event):
        try:
            # Get the values from the main window and the additional input
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            additional_value = float(additional_input.get())

            # Perform multiplication
            result = num1 * num2 * additional_value

            # Display the result in the popup window
            result_label.config(text=f'Result: {result}')

            # Also update the output string in the main window
            output_string.set(f'Result: {result}')
        except ValueError:
            result_label.config(text='Please enter valid numbers.')

    # Bind the Enter key to the handle_input function
    additional_input.bind('<Return>', handle_input)

    # Label to display the result
    result_label = ttk.Label(master=popup_window, text='', font='Calibri 14')
    result_label.pack(pady=10)
