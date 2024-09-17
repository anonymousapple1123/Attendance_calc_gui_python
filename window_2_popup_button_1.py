#latest push&commit at sep 17 10:10 am
import ttkbootstrap as ttk
import calc_file as w1_calc


def open_popup_button2(entry1, entry2, output_string):
    # Create a new window
    popup_window = ttk.Window(themename='journal')
    popup_window.title('Input leave')
    popup_window.geometry('900x450')

    # Label for the popup
    label = ttk.Label(master=popup_window, text='Input number of days you want to take leave :', font='Calibri 14')
    label.pack(pady=10)

    # Entry field for additional input
    additional_input = ttk.Entry(master=popup_window)
    additional_input.pack(pady=15)

    # Function to handle input and perform multiplication
    def handle_input(event):
        try:
            # Get the values from the main window and the additional input
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            additional_value = float(additional_input.get())

            # Perform multiplication
            result = w1_calc.need_leave(num1,num2,additional_value)

            # Display the result in the popup window
            result_label.config(text=f'Your attendance after leave : {result:.2f} %')

            # Also update the output string in the main window
            output_string.set(f'Your attendance after leave : {result:.2f} %')
        except ValueError:
            result_label.config(text='Please enter valid numbers.')

    # Bind the Enter key to the handle_input function
    additional_input.bind('<Return>', handle_input)

    # Label to display the result
    result_label = ttk.Label(master=popup_window, text='', font='Calibri 14')
    result_label.pack(pady=10)


def open_popup_button1(entry1, entry2, output_string):
    # Create a new window
    popup_window = ttk.Window(themename='journal')
    popup_window.title('Input leave')
    popup_window.geometry('950x550')

    # Label for the popup
    label = ttk.Label(master=popup_window, text='Input number of days you want to take leave and avoid fine:', font='Calibri 14')
    label.pack(pady=10)

    # Entry field for additional input
    additional_input = ttk.Entry(master=popup_window)
    additional_input.pack(pady=15)

    # Function to handle input and perform multiplication
    def handle_input(event):
        try:
            # Get the values from the main window and the additional input
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            additional_value = float(additional_input.get())

            # Perform multiplication
            result = w1_calc.avoid_fine(num1,num2,additional_value)

            # Display the result in the popup window
            result_label.config(text=f'Lecture to be present to avoid fine after your leave : {int(result)} lectures or {int(result/8)} days.')

            # Also update the output string in the main window
            output_string.set(f'Lecture to be present to avoid fine after your leave : {int(result)} lectures or {int(result/8)} days.')
        except ValueError:
            result_label.config(text='Please enter valid numbers.')

    # Bind the Enter key to the handle_input function
    additional_input.bind('<Return>', handle_input)

    # Label to display the result
    result_label = ttk.Label(master=popup_window, text='', font='Calibri 14')
    result_label.pack(pady=10)



def open_popup_button3(entry1, entry2, output_string):
    # Create a new window
    popup_window = ttk.Window(themename='journal')
    popup_window.title('Get Attendance')
    popup_window.geometry('900x450')

    # Label for the popup
    label = ttk.Label(master=popup_window, text='Input the percentage you want to reach :', font='Calibri 14')
    label.pack(pady=10)

    # Entry field for additional input
    additional_input = ttk.Entry(master=popup_window)
    additional_input.pack(pady=15)

    # Function to handle input and perform multiplication
    def handle_input(event):
        try:
            # Get the values from the main window and the additional input
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            additional_value = float(additional_input.get())

            # Perform multiplication
            result = w1_calc.get_attendance(num1,num2,additional_value)
            if result== -1.01:
                result_label.config(text=f'Not possible to reach that attendance.')
            elif result== -2.01:
                result_label.config(text=f'You attendance is already 100%.')
            elif result == -3.01:
                result_label.config(text=f'You already have that attendance.')
            elif result<0:
                result_label.config(text=f'Attend {int(-1*result)} lectures or {int((-1*result)/8)} days to get the desired attendance.')
            elif result>0:
                result_label.config(text=f'Attend {int(result)} lectures or {int((result)/8)} days to get the desired attendance.')

            # Also update the output string in the main window
            if result== -1.01:
                output_string.set(f'Not possible to reach that attendance.')
            elif result== -2.01:
                output_string.set(f'You attendance is already 100%.')
            elif result==-3.01:
                output_string.set(f'You already have that attendance.')
            elif result<0:
                output_string.set(f'Attend {int(-1*result)} lectures or {int(-1*result)/8} days to get the desired attendance.')
            elif result>0:
                output_string.set(f'Attend {int(result)} lectures or {int((result)/8)} days to get the desired attendance.')
            #output_string.set(f'Attend {result} lectures or {result/8} days to get the desired attendance.')
        except ValueError:
            result_label.config(text='Please enter valid numbers.')

    # Bind the Enter key to the handle_input function
    additional_input.bind('<Return>', handle_input)

    # Label to display the result
    result_label = ttk.Label(master=popup_window, text='', font='Calibri 14')
    result_label.pack(pady=10)
