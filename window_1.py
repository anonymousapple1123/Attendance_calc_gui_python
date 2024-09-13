import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def main_window():
    def convert():
        print(entry.get())
        output_string.set('test')
    #window
    window=ttk.Window(themename='journal')
    window.title('ARNAVVV')
    window.geometry('700x450')

    #
    title_label=ttk.Label(master =window, text='Chota bhai>>>',font='Calibri 24 bold')
    title_label.pack()

    #input field
    input_frame=ttk.Frame(master=window)
    entry_int=tk.IntVar()
    entry=ttk.Entry(master=input_frame,textvariable=entry_int)
    button=ttk.Button(master=input_frame,text='Convert',command=convert)
    entry.pack()
    button.pack()
    input_frame.pack(pady=50)

    #output
    output_string=tk.StringVar()
    output_label=ttk.Label(master=window,text='Output',
                           font='Calibri 24',
                           textvariable=output_string)
    output_label.pack(pady=15)
    #run
    window.mainloop()
