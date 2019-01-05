#! python3
# January 20, 2018
# Denniel Luis Saway Sadian

from tkinter import *
from tkinter import ttk, font, messagebox


class IdealGasLawSolver(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding='3 5 3 3')
        self.root = master
        # objects
        self.p = StringVar()
        self.v = StringVar()
        self.n = StringVar()
        self.r = StringVar()
        self.t = StringVar()
        self.to_find_term = StringVar()
        self.top_terms = StringVar()
        self.bottom_term = StringVar()
        self.top_numbers = StringVar()
        self.bottom_numbers = StringVar()
        self.bottom_number = StringVar()
        self.top_number = StringVar()
        self.answer = StringVar()
        self.separator = StringVar()
        # geometry management
        for i in range(13):
            self.rowconfigure(i, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.widgets()

    def process(self):
        """ PV = nRT """
        try:
            if self.p.get() in '? ':
                self.to_find_term.set('P =')
                self.top_terms.set('n R T')
                self.bottom_term.set('V')
                self.top_numbers.set(f'{self.n.get()} ({self.r.get()}) '
                                     f'({self.t.get()})')
                self.top_number.set(round(float(self.n.get())
                                          * float(self.r.get())
                                          * float(self.t.get()), 4))
                self.bottom_numbers.set(self.v.get())
                self.bottom_number.set(self.v.get())
            elif self.v.get() in '? ':
                self.to_find_term.set('V =')
                self.top_terms.set('n R T')
                self.bottom_term.set('P')
                self.top_numbers.set(f'{self.n.get()} ({self.r.get()}) '
                                     f'({self.t.get()})')
                self.top_number.set(round(float(self.n.get())
                                          * float(self.r.get())
                                          * float(self.t.get()), 4))
                self.bottom_numbers.set(self.p.get())
                self.bottom_number.set(self.p.get())
            elif self.n.get() in '? ':
                self.to_find_term.set('n =')
                self.top_terms.set('P V')
                self.bottom_term.set('R T')
                self.top_numbers.set(f'{self.p.get()} ({self.v.get()}) ')
                self.top_number.set(round(float(self.p.get())
                                          * float(self.v.get()), 4))
                self.bottom_numbers.set(f'{self.r.get()} ({self.t.get()})')
                self.bottom_number.set(round(float(self.r.get())
                                             * float(self.t.get()), 4))
            elif self.r.get() in '? ':
                self.to_find_term.set('R =')
                self.top_terms.set('P V')
                self.bottom_term.set('n T')
                self.top_numbers.set(f'{self.p.get()} ({self.v.get()}) ')
                self.top_number.set(round(float(self.p.get())
                                          * float(self.v.get()), 4))
                self.bottom_numbers.set(f'{self.n.get()} ({self.t.get()})')
                self.bottom_number.set(round(float(self.n.get())
                                             * float(self.t.get()), 4))
            elif self.t.get() in '? ':
                self.to_find_term.set('T =')
                self.top_terms.set('P V')
                self.bottom_term.set('n R')
                self.top_numbers.set(f'{self.p.get()} ({self.v.get()}) ')
                self.top_number.set(round(float(self.p.get())
                                          * float(self.v.get()), 4))
                self.bottom_numbers.set(f'{self.n.get()} ({self.r.get()})')
                self.bottom_number.set(round(float(self.n.get())
                                             * float(self.r.get()), 4))
            else:
                messagebox.showinfo('Info', 'Complete givens.')
                self.clear()
                return
            self.separator.set('-' * len(self.top_numbers.get()))
            y = round(float(self.top_number.get())
                      / float(self.bottom_number.get()), 4)
            self.answer.set(f'{self.to_find_term.get()} {y}')
        except ValueError:
            messagebox.showerror('Error', 'Value Error')
            self.clear()

    def clear(self):
        for i in [self.t, self.p, self.v,
                  self.top_terms, self.top_numbers, self.top_number,
                  self.bottom_numbers, self.bottom_term, self.to_find_term,
                  self.answer, self.separator, self.n,
                  self.r, self.bottom_number]:
            i.set('')

    def widgets(self):
        ttk.Label(self, text='Givens:').grid(column=0, row=0, columnspan=2)
        ttk.Label(self, text='Pressure (P):').grid(
            column=0, row=1, sticky=E)
        ttk.Entry(self, textvariable=self.p).grid(column=1, row=1, sticky='WE')
        ttk.Label(self, text='Volume (V):').grid(
            column=0, row=2, sticky=E)
        ttk.Entry(self, textvariable=self.v).grid(column=1, row=2, sticky='WE')
        ttk.Label(self, text='Number of Moles (n):').grid(
            column=0, row=3, sticky=E)
        ttk.Entry(self, textvariable=self.n).grid(column=1, row=3, sticky='WE')
        ttk.Label(self, text='Universal Gas Constant (R):').grid(
            column=0, row=4, sticky=E)
        ttk.Entry(self, textvariable=self.r).grid(column=1, row=4, sticky='WE')
        ttk.Label(self, text='Temperature (T):').grid(
            column=0, row=5, sticky=E)
        ttk.Entry(self, textvariable=self.t).grid(column=1, row=5, sticky='WE')
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=6, columnspan=2, sticky='WE', pady=10)
        ttk.Button(self, text='Process', command=self.process).grid(
            column=0, row=7, columnspan=2, sticky='WE')
        ttk.Button(self, text='Clear', command=self.clear).grid(
            column=0, row=8, columnspan=2, sticky='WE')
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=9, columnspan=2, sticky='WE', pady=10)
        ttk.Label(self, text="Direction:\n"
                             "Leave the field of the missing term\n"
                             "empty or just type '?' in finding it.").grid(
            column=0, row=10, columnspan=2, rowspan=3)
        ttk.Separator(self, orient=VERTICAL).grid(
            column=2, row=0, rowspan=13, sticky='NS', padx=10)
        ttk.Label(self, text='Solution:').grid(column=3, row=0, columnspan=2)
        ttk.Label(self, textvariable=self.to_find_term).grid(column=3, row=2)
        ttk.Label(self, textvariable=self.top_terms).grid(
            column=4, row=1, sticky=S)
        ttk.Label(self, textvariable=self.separator).grid(
            column=4, row=2)
        ttk.Label(self, textvariable=self.bottom_term).grid(
            column=4, row=3, sticky=N)
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=3, row=4, columnspan=2, sticky='WE', pady=10)
        ttk.Label(self, textvariable=self.to_find_term).grid(column=3, row=6)
        ttk.Label(self, textvariable=self.top_numbers).grid(
            column=4, row=5, sticky=S)
        ttk.Label(self, textvariable=self.separator).grid(
            column=4, row=6)
        ttk.Label(self, textvariable=self.bottom_numbers).grid(
            column=4, row=7, sticky=N)
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=3, row=8, columnspan=2, sticky='WE', pady=10)
        ttk.Label(self, textvariable=self.to_find_term).grid(column=3, row=10)
        ttk.Label(self, textvariable=self.top_number).grid(
            column=4, row=9, sticky=S)
        ttk.Label(self, textvariable=self.separator).grid(
            column=4, row=10)
        ttk.Label(self, textvariable=self.bottom_number).grid(
            column=4, row=11, sticky=N)
        ttk.Label(self, textvariable=self.answer).grid(
            column=3, row=12, columnspan=2, pady='20 0')


if __name__ == '__main__':
    root = Tk()
    app = IdealGasLawSolver(root)
    app.grid(column=0, row=0, sticky='NEWS')
    text = font.Font(family='Segoe Print', size=11, weight='bold')
    ttk.Style().configure('TFrame', background='lightgreen')
    ttk.Style().configure('TLabel', font=text, background='lightgreen')
    ttk.Style().configure('TButton', font=text, background='lightgreen')
    root.title("Ideal Gas Law")
    root.mainloop()
