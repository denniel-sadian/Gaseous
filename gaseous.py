#! python3
# January 20, 2018
# Denniel Luis Saway Sadian

from tkinter import *
from tkinter import ttk, font, messagebox
from boyle import LawOfBoyleSolver
from charles import LawOfCharlesSolver
from avogadro import LawOfAvogadroSolver
from combined import CombinedGasLawSolver
from ideal import IdealGasLawSolver
from gaylussac import LawOfGayLussacSolver
from unitconverter import UnitConverter
from elements_gui import ElementsGui
from about_dialog import AboutDialog


class Gaseous(ttk.Notebook):

    def __init__(self, master):
        ttk.Notebook.__init__(self, master, padding='3 5 3 3')
        self.root = master
        # pages
        self.p1 = ttk.Frame(self, relief='groove', padding=8)
        self.p2 = ttk.Frame(self, relief='groove', padding=8)
        self.p3 = ttk.Frame(self, relief='groove', padding=8)
        self.p4 = ttk.Frame(self, relief='groove', padding=8)
        self.p5 = ttk.Frame(self, relief='groove', padding=8)
        self.p6 = ttk.Frame(self, relief='groove', padding=8)
        self.p7 = ttk.Frame(self, relief='groove', padding=8)
        self.p8 = ttk.Frame(self, relief='groove', padding=8)
        self.p9 = ttk.Frame(self, relief='groove')
        self.add(self.p1, text='Home', padding=2)
        self.add(self.p2, text='Boyle', padding=2)
        self.add(self.p3, text='Charles', padding=2)
        self.add(self.p4, text='Combined', padding=2)
        self.add(self.p5, text='Avogadro', padding=2)
        self.add(self.p6, text='Ideal', padding=2)
        self.add(self.p7, text='Gay-Lussac', padding=2)
        self.add(self.p8, text='Converter', padding=2)
        self.add(self.p9, text='Elements', padding=2)
        # objects
        self.boyle = LawOfBoyleSolver(self.p2)
        self.charles = LawOfCharlesSolver(self.p3)
        self.combined = CombinedGasLawSolver(self.p4)
        self.avogadro = LawOfAvogadroSolver(self.p5)
        self.ideal = IdealGasLawSolver(self.p6)
        self.lussac = LawOfGayLussacSolver(self.p7)
        self.converter = UnitConverter(self.p8)
        self.elements_widgets = ElementsGui(self.p9)
        self._p1 = StringVar()
        self._p2 = StringVar()
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.t1 = StringVar()
        self.t2 = StringVar()
        self.n1 = StringVar()
        self.n2 = StringVar()
        self.r = StringVar()
        # geometry management
        for i in range(15):
            self.rowconfigure(i, weight=1)
            self.p1.rowconfigure(i, weight=1)
            self.p2.rowconfigure(i, weight=1)
            self.p3.rowconfigure(i, weight=1)
            self.p4.rowconfigure(i, weight=1)
            self.p5.rowconfigure(i, weight=1)
            self.p6.rowconfigure(i, weight=1)
            self.p7.rowconfigure(i, weight=1)
            self.p8.rowconfigure(i, weight=1)
            self.p9.rowconfigure(i, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
            self.p1.columnconfigure(i, weight=1)
            self.p2.columnconfigure(i, weight=1)
            self.p3.columnconfigure(i, weight=1)
            self.p4.columnconfigure(i, weight=1)
            self.p5.columnconfigure(i, weight=1)
            self.p6.columnconfigure(i, weight=1)
            self.p7.columnconfigure(i, weight=1)
            self.p8.columnconfigure(i, weight=1)
            self.p9.columnconfigure(i, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        # events
        self.root.bind('<Key>', self.do_key_functions)
        self.root.bind('<Return>', self.decide)
        self.converter.input.bind('<Return>', self.converter.convert)
        self.root.bind('<F1>', self.f1)

        self.widgets()

    def do_key_functions(self, *args):
        self.elements_widgets.find_element()
        self.converter.convert()
        return args

    @staticmethod
    def all_in(x, y):
        z = 0
        for i in x:
            if i in y:
                z += 1
        return z, len(x) == z

    def f1(self, *args):
        AboutDialog(self.master, window_title='About Gaseous',
                    about_title='Gaseous',
                    content='Developed and written by:\n'
                            '\tDenniel Luis Saway Sadian '
                            '(https://denniel-sadian.github.io)\n\n'
                            'Date of creation:\n'
                            '\tJanuary 21, 2018\n\n'
                            'Description:\n'
                            '\tThis application is written for quicker solving '
                            'of gas problems. When using this application,'
                            ' make sure that all the givens are compatible '
                            'with each other. For example, if the initial '
                            'volume is in liters, the final volume must be in '
                            'liters as well. The desired unit for temperature '
                            'is kelvin. This app has a built-in unit converter, '
                            'so conversion is easy.\n'
                            '\tThis application is written completely in Python '
                            'Programming Language. It uses Tkinter as the GUI '
                            'Framework.',
                    image='gas.png').mainloop()
        return args

    def decide(self, *args):
        has_values = []
        for i in [('p1', self._p1), ('p2', self._p2), ('v1', self.v1),
                  ('v2', self.v2), ('t1', self.t1), ('t2', self.t2),
                  ('n1', self.n1), ('n2', self.n2), ('r', self.r)]:
            if i[1].get():
                has_values.append(i[0])
        if self.all_in(has_values, ['p1', 'v1', 'p2', 'v2']) == (3, True):
            self.boyle.clear()
            if self._p1.get():
                self.boyle.p1.set(self._p1.get())
            if self._p2.get():
                self.boyle.p2.set(self._p2.get())
            if self.v1.get():
                self.boyle.v1.set(self.v1.get())
            if self.v2.get():
                self.boyle.v2.set(self.v2.get())
            self.select(1)
            self.boyle.process()
        elif self.all_in(has_values, ['v1', 'v2', 't1', 't2']) == (3, True):
            self.charles.clear()
            if self.v1.get():
                self.charles.v1.set(self.v1.get())
            if self.v2.get():
                self.charles.v2.set(self.v2.get())
            if self.t1.get():
                self.charles.t1.set(self.t1.get())
            if self.t2.get():
                self.charles.t2.set(self.t2.get())
            self.select(2)
            self.charles.process()
        elif self.all_in(has_values, ['p1', 'p2', 'v1', 'v2', 't1', 't2']) \
                == (5, True):
            self.combined.clear()
            if self._p1.get():
                self.combined.p1.set(self._p1.get())
            if self._p2.get():
                self.combined.p2.set(self._p2.get())
            if self.v1.get():
                self.combined.v1.set(self.v1.get())
            if self.v2.get():
                self.combined.v2.set(self.v2.get())
            if self.t1.get():
                self.combined.t1.set(self.t1.get())
            if self.t2.get():
                self.combined.t2.set(self.t2.get())
            self.select(3)
            self.combined.process()
        elif self.all_in(has_values, ['v1', 'v2', 'n1', 'n2']) == (3, True):
            self.avogadro.clear()
            if self.v1.get():
                self.avogadro.v1.set(self.v1.get())
            if self.v2.get():
                self.avogadro.v2.set(self.v2.get())
            if self.n1.get():
                self.avogadro.n1.set(self.n1.get())
            if self.n2.get():
                self.avogadro.n2.set(self.n2.get())
            self.select(4)
            self.avogadro.process()
        elif self.all_in(has_values, ['p1', 'p2', 'v1', 'v2', 'n1', 'n2',
                                      't1', 't2', 'r']) == (4, True):
            self.ideal.clear()
            if self._p1.get():
                self.ideal.p.set(self._p1.get())
            if self._p2.get():
                self.ideal.p.set(self._p2.get())
            if self.v1.get():
                self.ideal.v.set(self.v1.get())
            if self.v2.get():
                self.ideal.v.set(self.v2.get())
            if self.n1.get():
                self.ideal.n.set(self.n1.get())
            if self.n2.get():
                self.ideal.n.set(self.n2.get())
            if self.r.get():
                self.ideal.r.set(self.r.get())
            if self.t1.get():
                self.ideal.t.set(self.t1.get())
            if self.t2.get():
                self.ideal.t.set(self.t2.get())
            self.select(5)
            self.ideal.process()
        elif self.all_in(has_values, ['p1', 't1', 'p2', 't2']) == (3, True):
            self.lussac.clear()
            if self._p1.get():
                self.lussac.p1.set(self._p1.get())
            if self._p2.get():
                self.lussac.p2.set(self._p2.get())
            if self.t1.get():
                self.lussac.t1.set(self.t1.get())
            if self.t2.get():
                self.lussac.t2.set(self.t2.get())
            self.select(6)
            self.lussac.process()
        elif len(has_values) == 0:
            return args
        else:
            messagebox.showinfo(
                'Info', 'The program cannot decide what law must be applied. '
                        'Make sure the givens are correct and clean')
        self.clear()
        return args

    def clear(self):
        for i in [self._p1, self._p2, self.v1, self.v2, self.t1, self.t2,
                  self.n1, self.n2, self.r]:
            i.set('')

    def widgets(self):
        # p1
        ttk.Label(self.p1, text='Gas Problem Solver', style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p1, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        ttk.Label(self.p1, text='Givens:').grid(column=0, row=2, columnspan=5)
        ttk.Label(self.p1, text='Initial Pressure (P1):').grid(
            column=1, row=3, sticky=E)
        ttk.Entry(self.p1, textvariable=self._p1).grid(
            column=2, row=3, sticky='WE')
        ttk.Label(self.p1, text='Final Pressure (P2):').grid(
            column=1, row=4, sticky=E)
        ttk.Entry(self.p1, textvariable=self._p2).grid(
            column=2, row=4, sticky='WE')
        ttk.Label(self.p1, text='Initial Volume (V1):').grid(
            column=1, row=5, sticky=E)
        ttk.Entry(self.p1, textvariable=self.v1).grid(
            column=2, row=5, sticky='WE')
        ttk.Label(self.p1, text='Final Volume (V2):').grid(
            column=1, row=6, sticky=E)
        ttk.Entry(self.p1, textvariable=self.v2).grid(
            column=2, row=6, sticky='WE')
        ttk.Label(self.p1, text='Initial Temperature (T1):').grid(
            column=1, row=7, sticky=E)
        ttk.Entry(self.p1, textvariable=self.t1).grid(
            column=2, row=7, sticky='WE')
        ttk.Label(self.p1, text='Final Temperature (T2):').grid(
            column=1, row=8, sticky=E)
        ttk.Entry(self.p1, textvariable=self.t2).grid(
            column=2, row=8, sticky='WE')
        ttk.Label(self.p1, text='Initial Number of Moles (n1):').grid(
            column=1, row=9, sticky=E)
        ttk.Entry(self.p1, textvariable=self.n1).grid(
            column=2, row=9, sticky='WE')
        ttk.Label(self.p1, text='Final Number of Moles (n2):').grid(
            column=1, row=10, sticky=E)
        ttk.Entry(self.p1, textvariable=self.n2).grid(
            column=2, row=10, sticky='WE')
        ttk.Label(self.p1, text='Universal Gas Constant (R):').grid(
            column=1, row=11, sticky=E)
        ttk.Entry(self.p1, textvariable=self.r).grid(
            column=2, row=11, sticky='WE')
        ttk.Separator(self.p1, orient=HORIZONTAL).grid(
            column=0, row=12, sticky='WE', columnspan=5)
        ttk.Button(self.p1, text='Decide', command=self.decide).grid(
            column=0, row=13, columnspan=5, sticky='WE')
        ttk.Button(self.p1, text='Clear', command=self.clear).grid(
            column=0, row=14, columnspan=5, sticky='WE')
        # p2
        ttk.Label(self.p2, text="Boyle's Law", style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p2, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        self.boyle.grid(column=0, row=2, sticky='NEWS', columnspan=5, rowspan=13)
        # p3
        ttk.Label(self.p3, text="Charles' Law", style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p3, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        self.charles.grid(column=0, row=2, sticky='NEWS',
                          columnspan=5, rowspan=13)
        # p4
        ttk.Label(self.p4, text="Combined Gas Law", style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p4, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        self.combined.grid(column=0, row=2, sticky='NEWS',
                           columnspan=5, rowspan=13)
        # p5
        ttk.Label(self.p5, text="Avogadro's Law", style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p5, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        self.avogadro.grid(column=0, row=2, sticky='NEWS',
                           columnspan=5, rowspan=13)
        # p6
        ttk.Label(self.p6, text="Ideal Gas Law", style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p6, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        self.ideal.grid(column=0, row=2, sticky='NEWS', columnspan=5, rowspan=13)
        # p7
        ttk.Label(self.p7, text="Gay-Lussac's Law", style='Head.TLabel').grid(
            column=0, row=0, columnspan=5)
        ttk.Separator(self.p7, orient=HORIZONTAL).grid(
            column=0, row=1, sticky='WE', columnspan=5)
        self.lussac.grid(column=0, row=2, sticky='NEWS',
                         columnspan=5, rowspan=13)
        # p8
        self.converter.grid(
            column=0, row=0, sticky='NEWS', columnspan=5, rowspan=15)
        # p9
        self.elements_widgets.grid(
            column=0, row=0, sticky='NEWS', columnspan=5, rowspan=15)


if __name__ == '__main__':
    root = Tk()
    app = Gaseous(root)
    app.grid(column=0, row=0, sticky='NEWS')
    text = font.Font(family='Segoe Print', size=11, weight='bold')
    _text = font.Font(size=10)
    head = font.Font(family='Segoe Print', size=18, weight='bold')
    _head = font.Font(size=18)
    ttk.Style().configure('TFrame', background='lightgreen')
    ttk.Style().configure('TNotebook', background='green')
    ttk.Style().configure('TLabel', font=text, background='lightgreen')
    ttk.Style().configure('Head.TLabel', font=head, background='lightgreen')
    ttk.Style().configure('ElementsHeading.TLabel', font=head)
    ttk.Style().configure('HeadTop.TLabel', font=_head, background='#e4e4e4')
    ttk.Style().configure('Text.TLabel', font=_text, background='#e4e4e4')
    ttk.Style().configure('TButton', font=text, background='lightgreen')
    root.title("Gaseous")
    try:
        root.wm_iconbitmap('gas.ico')
    except TclError:
        print("Does not support icons.")
    root.mainloop()
