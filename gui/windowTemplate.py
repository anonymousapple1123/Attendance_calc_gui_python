import tkinter as tk
import ttkbootstrap as ttk

def create_gradient_background(canvas, width, height):
    """
    Creates a very light gradient background from very light purple to white.
    """
    for i in range(height):
        r = 255  # Red remains constant
        g = int(240 - (240 * (i / height)))  # Green transitions from 240 to 0
        b = 255  # Blue remains constant
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(0, i, width, i, fill=color)

def draw_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """
    Draw a rounded rectangle on the canvas.
    """
    # Top-left corner
    canvas.create_arc(x1, y1, x1 + radius * 2, y1 + radius * 2, start=90, extent=90, **kwargs)
    # Top-right corner
    canvas.create_arc(x2 - radius * 2, y1, x2, y1 + radius * 2, start=0, extent=90, **kwargs)
    # Bottom-left corner
    canvas.create_arc(x1, y2 - radius * 2, x1 + radius * 2, y2, start=180, extent=90, **kwargs)
    # Bottom-right corner
    canvas.create_arc(x2 - radius * 2, y2 - radius * 2, x2, y2, start=270, extent=90, **kwargs)
    # Center rectangles to connect the arcs
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, **kwargs)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, **kwargs)

def main_window_template(config):
    """
    Creates the main window for the Attendance Calculator.

    The config dictionary should contain keys for setting most variables, for example:
      - theme: ttkbootstrap theme name
      - title: window title
      - geometry: window geometry (e.g., '1480x850')
      - window_width, window_height: dimensions for the canvas
      - title_text: text for the title label
      - title_font: font settings for the title
      - label_background: background color for labels
      - padding: padding for the input frame
      - entry_font: font for the entry fields
      - entry_width: width for the entry fields
      - output_font: font for the output label
      - calculate_button_text: text for the calculate button
      - calculate_button_style: bootstyle for the calculate button
      - button1_text, button2_text, button3_text: texts for the additional buttons
      - button_style: bootstyle for the additional buttons
      - button_width: width for the additional buttons
      - calc_function: a function that accepts two numbers and returns the attendance percentage
      - popup_function: a function to call that shows an initial popup (if needed)
      - popup_functions: a dict with keys 'button1', 'button2', and 'button3' for corresponding popup actions.
    """
    # Create the main window with the specified theme
    window = ttk.Window(themename=config.get('theme', 'flatly'))
    window.title(config.get('title', 'Attendance Calculator'))
    window.geometry(config.get('geometry', '1480x850'))

    # Create a canvas with a gradient background
    width = config.get('window_width', 1480)
    height = config.get('window_height', 850)
    canvas = tk.Canvas(window, width=width, height=height)
    canvas.pack(fill="both", expand=True)
    create_gradient_background(canvas, width, height)

    # Title label
    title_label = ttk.Label(
        master=window,
        text=config.get('title_text', 'Calculate Attendance Percentage'),
        font=config.get('title_font', 'Helvetica 24 bold'),
        background=config.get('label_background', 'white')
    )
    title_label.place(relx=0.5, rely=0.05, anchor='center')

    # Call the popup function if provided
    popup_fn = config.get('popup_function')
    if popup_fn:
        popup_fn()

    # Create an input frame
    input_frame = ttk.Frame(master=window, padding=config.get('padding', 20))
    input_frame.place(relx=0.5, rely=0.3, anchor='center')

    # Input fields
    entry1 = ttk.Entry(
        master=input_frame,
        font=config.get('entry_font', 'Helvetica 16'),
        width=config.get('entry_width', 20)
    )
    entry1.pack(pady=10, padx=10)

    entry2 = ttk.Entry(
        master=input_frame,
        font=config.get('entry_font', 'Helvetica 16'),
        width=config.get('entry_width', 20)
    )
    entry2.pack(pady=10, padx=10)

    # Output label and variable
    output_string = tk.StringVar()
    output_label = ttk.Label(
        master=window,
        text='Output',
        font=config.get('output_font', 'Helvetica 24'),
        textvariable=output_string,
        background=config.get('label_background', 'white')
    )
    output_label.place(relx=0.5, rely=0.8, anchor='center')

    # Define button command for calculating attendance
    def calculate_attendance():
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result = config.get('calc_function', lambda a, b: 0)(num1, num2)
            output_string.set(f'Attendance: {result:.2f} %')
        except ValueError:
            output_string.set('Please enter valid numbers.')

    # Wrappers for the popup functions (if provided)
    popup_funcs = config.get('popup_functions', {})

    def button1_action():
        fn = popup_funcs.get('button1')
        if fn:
            fn(entry1, entry2, output_string)

    def button2_action():
        fn = popup_funcs.get('button2')
        if fn:
            fn(entry1, entry2, output_string)

    def button3_action():
        fn = popup_funcs.get('button3')
        if fn:
            fn(entry1, entry2, output_string)

    # Calculate Attendance button
    calculate_button = ttk.Button(
        master=input_frame,
        text=config.get('calculate_button_text', 'Calculate Attendance'),
        command=calculate_attendance,
        bootstyle=config.get('calculate_button_style', 'primary'),
        width=config.get('button_width', 20)
    )
    calculate_button.pack(pady=10)

    # Additional buttons
    button1 = ttk.Button(
        master=input_frame,
        text=config.get('button1_text', 'Avoid Fine'),
        command=button1_action,
        bootstyle=config.get('button_style', 'info'),
        width=config.get('button_width', 20)
    )
    button1.pack(pady=5)

    button2 = ttk.Button(
        master=input_frame,
        text=config.get('button2_text', 'Take Leave'),
        command=button2_action,
        bootstyle=config.get('button_style', 'info'),
        width=config.get('button_width', 20)
    )
    button2.pack(pady=5)

    button3 = ttk.Button(
        master=input_frame,
        text=config.get('button3_text', 'Get Attendance'),
        command=button3_action,
        bootstyle=config.get('button_style', 'info'),
        width=config.get('button_width', 20)
    )
    button3.pack(pady=5)

    # Start the main loop
    window.mainloop()
