#! python3
# December 30, 2017

from tkinter import *
from tkinter import ttk, font
from units import *


class UnitConverter(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding='10 10 10 0', relief='flat')
        self.root = master
        # styles
        self.style = ttk.Style()
        self.heading = font.Font(family='Segoe Print', size=25, weight='bold')
        self.text = font.Font(family='Segoe Print', size=15, weight='bold')
        self.combo_text = font.Font(family='Comic Sans MS', size=12)
        self.text_label = font.Font(family='Comic Sans MS', size=15,
                                    weight='bold')
        self.style.configure('TFrame', background='lightgreen')
        self.style.configure('To.TLabel', background='lightblue',
                             font=self.text_label)
        self.style.configure('TLabel', font=self.text,
                             padding=5, background='lightgreen')
        # objects
        self.chosen_conversion = StringVar()
        self.first_chosen = StringVar()
        self.second_chosen = StringVar()
        self.input_value = StringVar()
        self.input = ttk.Entry(self, textvariable=self.input_value,
                               font=self.combo_text)
        self.conversion = ttk.Combobox(self, textvariable=self.chosen_conversion,
                                       font=self.combo_text)
        self.first_unit = ttk.Combobox(self, textvariable=self.first_chosen,
                                       font=self.combo_text)
        self.second_unit = ttk.Combobox(self, textvariable=self.second_chosen,
                                        font=self.combo_text)
        self.conversion['values'] = AVAILABLE
        self.to_label = ttk.Label(self, text='Hello World!', style='To.TLabel')
        # geometry management
        for i in range(3):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        # event bindings
        self.conversion.bind('<<ComboboxSelected>>',
                             self.get_selected_conversion)
        self.second_unit.bind('<<ComboboxSelected>>', self.convert)
        self.first_unit.bind('<<ComboboxSelected>>', self.convert)
        self.root.bind('<Key>', self.convert)
        self.root.bind('<Return>', self.convert)

        self.widgets()

    def get_selected_conversion(self, event=None):
        self.first_unit.set('')
        self.second_unit.set('')
        self.first_unit['values'] = tuple(CONVERSIONS[self.chosen_conversion.
                                          get()].keys())
        self.second_unit['values'] = tuple(CONVERSIONS[self.chosen_conversion.
                                           get()].keys())
        return event

    def convert(self, event=None):
        try:
            if self.input_value.get() and self.first_chosen.get() \
                    and self.second_chosen.get():
                if self.second_chosen.get() not in 'celsius fahrenheit kelvin':
                    self.to_label['text'] = float(
                        self.input_value.get()
                    ) * CONVERSIONS[self.chosen_conversion.get(
                                            )][self.first_chosen.get(
                                            )][self.second_chosen.get()]
                else:
                    self.to_label['text'] = \
                        CONVERSIONS[self.chosen_conversion.get(
                                            )][self.first_chosen.get(
                                            )][self.second_chosen.get()](
                        float(self.input_value.get()))
                self.to_label['text'] = f"{self.to_label['text']:,}"
            else:
                self.to_label['text'] = ""
            self.style.configure('TFrame', background='lightgreen')
            self.style.configure('TLabel', background='lightgreen')
            self.style.configure('To.TLabel', background='lightblue')
        except ValueError:
            self.to_label['text'] = 'Value Error'
            self.style.configure('TFrame', background='lightgray')
            self.style.configure('TLabel', background='lightgray')
            self.style.configure('To.TLabel', background='pink')
        return event

    def widgets(self):
        ttk.Label(self, text='Unit Converter', font=self.heading).grid(
            column=0, row=0, columnspan=3)
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=3, pady='0 10')
        ttk.Label(self, text='Conversion').grid(column=0, row=2)
        self.conversion.grid(column=1, row=2, sticky='WE', columnspan=2)
        ttk.Label(self, text='From').grid(column=0, row=3)
        self.input.grid(column=1, row=3, sticky='WE', padx='0 5')
        self.first_unit.grid(column=2, row=3, sticky='WE')
        ttk.Label(self, text='To').grid(column=0, row=4)
        self.to_label.grid(column=1, row=4, sticky='WE', padx='0 5')
        self.second_unit.grid(column=2, row=4, sticky='WE')
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=5, sticky='WE', columnspan=3, pady=10)


if __name__ == '__main__':
    root = Tk()
    app = UnitConverter(root)
    app.grid(column=0, row=0, sticky='NEWS')
    root.title('Converter')
    root.mainloop()
