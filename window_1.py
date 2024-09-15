import tkinter as tk
import ttkbootstrap as ttk

def main_window():
    def convert():
        # Get the input from the entry field and print it
        print(entry.get())
        # Set the output string to a test value
        output_string.set(f'Converted Value: {entry.get()}')

    # Create the main window
    window = ttk.Window(themename='journal')
    window.title('ARNAVVV')
    window.geometry('700x450')

    # Title label
    title_label = ttk.Label(master=window, text='Chota bhai>>>', font='Calibri 24 bold')
    title_label.pack()

    # Input frame
    input_frame = ttk.Frame(master=window)
    entry_int = tk.StringVar()  # Use StringVar to allow for text input
    entry = ttk.Entry(master=input_frame, textvariable=entry_int)
    button = ttk.Button(master=input_frame, text='Convert', command=convert)
    entry.pack()
    button.pack()
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
