from tkinter import *
from tkinter import ttk, font
import elements


class ElementsGui(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding=5, style='ElementsFrame.TFrame')
        self.master = master
        # objects
        self.symbol_name = StringVar()
        self.symbol = StringVar()
        self.name = StringVar()
        self.electronic_configuration = StringVar()
        self.atomic_number = StringVar()
        self.oxidation_state = StringVar()
        self.melting_point = StringVar()
        self.boiling_point = StringVar()
        self.density = StringVar()
        self.electronegativity = StringVar()
        self.classification = StringVar()
        self.group = StringVar()
        self.bg = ''
        self.fg = 'black'
        # geometry management
        for i in range(17):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

        self.create_widgets()

    def clear(self):
        self.bg = 'lightgray'
        self.fg = 'black'
        self.symbol.set('')
        self.name.set('')
        self.atomic_number.set('')
        self.electronic_configuration.set('')
        self.oxidation_state.set('')
        self.melting_point.set('')
        self.boiling_point.set('')
        self.density.set('')
        self.electronegativity.set('')
        self.classification.set('')
        self.group.set('')

    def restyle(self):
        ttk.Style().configure('ElementsFrame.TFrame', background=self.bg)
        ttk.Style().configure('ElementsHeading.TLabel',
                              background=self.bg, foreground=self.fg)
        ttk.Style().configure('ElementsLabel.TLabel',
                              background=self.bg, foreground=self.fg)

    def find_element(self, *args):
        if self.symbol_name.get() or self.atomic_number.get():
            try:
                if self.symbol_name.get():
                    n = self.symbol_name.get()[0].upper() + \
                        self.symbol_name.get()[1:]
                    e = elements.find_element(n)
                else:
                    e = elements.find_element_by_atomic_number(
                        int(self.atomic_number.get()))
            except ValueError:
                self.atomic_number.set('')
                self.clear()
                self.bg = 'lightgray'
                self.fg = 'black'
                self.restyle()
                return args
            if e is not None:
                self.symbol.set(e['symbol'])
                self.name.set(e['name'])
                self.atomic_number.set(e['atomic number'])
                self.electronic_configuration.set(e['electronic configuration'])
                self.oxidation_state.set(e['oxidation state'])
                self.melting_point.set(e['melting point'])
                self.boiling_point.set(e['boiling point'])
                self.density.set(e['density'])
                self.electronegativity.set(e['electronegativity'])
                c = ''
                for i in e['classification']:
                    c += f'{i}, '
                self.classification.set(c[:-2])
                self.group.set(e['group'])
                if e['group'] == 'Alkali Metals':
                    self.bg = 'green'
                    self.fg = 'white'
                elif e['group'] == 'Alkaline Earth Metals':
                    self.bg = '#f9c65b'
                    self.fg = 'black'
                elif e['group'] == 'Early Transition Metals':
                    self.bg = 'lightblue'
                    self.fg = 'black'
                elif e['group'] == 'Late Transition Metals':
                    self.bg = 'maroon'
                    self.fg = 'white'
                elif e['group'] == 'Basic/Poor Metals':
                    self.bg = 'purple'
                    self.fg = 'white'
                elif e['group'] == 'Metalloids/Semi-metals':
                    self.bg = 'yellow'
                    self.fg = 'black'
                elif e['group'] == 'Non-Metals':
                    self.bg = 'pink'
                    self.fg = 'black'
                elif e['group'] == 'Halogens':
                    self.bg = 'lightgreen'
                    self.fg = 'black'
                elif e['group'] == 'Noble Gas':
                    self.bg = 'blue'
                    self.fg = 'white'
                elif e['group'] == 'Lanthanides':
                    self.bg = '#b3ff00'
                    self.fg = 'black'
                elif e['group'] == 'Actinides':
                    self.bg = 'orange'
                    self.fg = 'black'
            else:
                self.bg = 'lightgray'
                self.fg = 'black'
                self.clear()
        else:
            self.bg = 'lightgray'
            self.clear()
        self.restyle()
        return args

    def create_widgets(self):
        ttk.Label(self, text='Elements', style='ElementsHeading.TLabel').grid(
            column=0, row=0, columnspan=4)
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=4)
        ttk.Label(self, text='Find by:', style='ElementsLabel.TLabel').grid(
            column=0, row=2, columnspan=4)
        ttk.Label(self, text='Symbol or Name:',
                  style='ElementsLabel.TLabel').grid(column=0, row=3, sticky=E)
        ttk.Entry(self, textvariable=self.symbol_name).grid(
            column=1, row=3, columnspan=2, sticky='WE')
        ttk.Label(self, text='Atomic number:',
                  style='ElementsLabel.TLabel').grid(column=0, row=4, sticky=E)
        ttk.Entry(self, textvariable=self.atomic_number).grid(
            column=1, row=4, columnspan=2, sticky='WE')
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=5, sticky='WE', columnspan=4)
        ttk.Label(self, text='Name:', style='ElementsLabel.TLabel').grid(
            column=0, row=6, sticky=E)
        ttk.Label(self, text='Symbol:', style='ElementsLabel.TLabel').grid(
            column=0, row=7, sticky=E)
        ttk.Label(self, text='Atomic number:',
                  style='ElementsLabel.TLabel').grid(column=0, row=8, sticky=E)
        ttk.Label(self, text='Electronic configuration:',
                  style='ElementsLabel.TLabel').grid(column=0, row=9, sticky=E)
        ttk.Label(self, text='Oxidation state:',
                  style='ElementsLabel.TLabel').grid(column=0, row=10, sticky=E)
        ttk.Label(self, text='Melting point:',
                  style='ElementsLabel.TLabel').grid(column=0, row=11, sticky=E)
        ttk.Label(self, text='boiling point:',
                  style='ElementsLabel.TLabel').grid(column=0, row=12, sticky=E)
        ttk.Label(self, text='Density:', style='ElementsLabel.TLabel').grid(
            column=0, row=13, sticky=E)
        ttk.Label(self, text='Electronegativity:',
                  style='ElementsLabel.TLabel').grid(column=0, row=14, sticky=E)
        ttk.Label(self, text='Classification:',
                  style='ElementsLabel.TLabel').grid(column=0, row=15, sticky=E)
        ttk.Label(self, text='Group:', style='ElementsLabel.TLabel').grid(
            column=0, row=16, sticky=E)
        ttk.Label(self, textvariable=self.name,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=6, columnspan=2)
        ttk.Label(self, textvariable=self.symbol,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=7, columnspan=2)
        ttk.Label(self, textvariable=self.atomic_number,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=8, columnspan=2)
        ttk.Label(self, textvariable=self.electronic_configuration,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=9, columnspan=2)
        ttk.Label(self, textvariable=self.oxidation_state,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=10, columnspan=2)
        ttk.Label(self, textvariable=self.melting_point,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=11, columnspan=2)
        ttk.Label(self, textvariable=self.boiling_point,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=12, columnspan=2)
        ttk.Label(self, textvariable=self.density,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=13, columnspan=2)
        ttk.Label(self, textvariable=self.electronegativity,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=14, columnspan=2)
        ttk.Label(self, textvariable=self.classification,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=15, columnspan=2)
        ttk.Label(self, textvariable=self.group,
                  style='ElementsLabel.TLabel').grid(
            column=1, row=16, columnspan=2)


if __name__ == '__main__':
    root = Tk()
    text = font.Font(family='Segoe Print', size=11, weight='bold')
    head = font.Font(family='Segoe Print', size=18, weight='bold')
    ttk.Style().configure('ElementsHeading.TLabel', font=head)
    ttk.Style().configure('ElementsFrame.TFrame')
    ttk.Style().configure('ElementsLabel.TLabel', font=text)
    ttk.Style().configure('TButton',  font=text)
    app = ElementsGui(root)
    app.grid(column=0, row=0, sticky='NEWS')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.bind('<Key>', app.find_element)
    root.title('Elements')
    root.mainloop()
