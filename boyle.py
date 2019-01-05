#! python3
# January 20, 2018
# Denniel Luis Saway Sadian

from tkinter import *
from tkinter import ttk, font, messagebox


class LawOfBoyleSolver(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding='3 5 3 3')
        self.root = master
        # objects
        self.p1 = StringVar()
        self.p2 = StringVar()
        self.v1 = StringVar()
        self.v2 = StringVar()
        self.to_find_term = StringVar()
        self.top_terms = StringVar()
        self.bottom_term = StringVar()
        self.top_numbers = StringVar()
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
        """ P1V1 = P2V2 """
        try:
            if self.p1.get() in '? ':
                self.to_find_term.set('P1 =')
                self.top_terms.set('P2 V2')
                self.bottom_term.set('V1')
                self.top_numbers.set(f'{self.p2.get()} ({self.v2.get()})')
                self.bottom_number.set(self.v1.get())
                self.top_number.set(round(float(self.p2.get())
                                          * float(self.v2.get()), 4))
            elif self.p2.get() in '? ':
                self.to_find_term.set('P2 =')
                self.top_terms.set('P1 V1')
                self.bottom_term.set('V2')
                self.top_numbers.set(f'{self.p1.get()} ({self.v1.get()})')
                self.bottom_number.set(self.v2.get())
                self.top_number.set(round(float(self.p1.get())
                                          * float(self.v1.get()), 4))
            elif self.v1.get() in '? ':
                self.to_find_term.set('V1 =')
                self.top_terms.set('P2 V2')
                self.bottom_term.set('P1')
                self.top_numbers.set(f'{self.p2.get()} ({self.v2.get()})')
                self.bottom_number.set(self.p1.get())
                self.top_number.set(round(float(self.p2.get())
                                          * float(self.v2.get()), 4))
            elif self.v2.get() in '? ':
                self.to_find_term.set('V2 =')
                self.top_terms.set('P1 V1')
                self.bottom_term.set('P2')
                self.top_numbers.set(f'{self.p1.get()} ({self.v1.get()})')
                self.bottom_number.set(self.p2.get())
                self.top_number.set(round(float(self.p1.get())
                                          * float(self.v1.get()), 4))
            else:
                messagebox.showinfo('Info', 'Complete givens.')
                self.clear()
                return
            self.separator.set('-' * (len(self.top_numbers.get())))
            x = round(float(self.top_number.get())
                      / float(self.bottom_number.get()), 4)
            self.answer.set(f'{self.to_find_term.get()} {x}')
        except ValueError:
            self.clear()
            messagebox.showerror('Error', 'Value Error')

    def clear(self):
        for i in [self.p1, self.v1, self.p2, self.v2,
                  self.top_terms, self.top_numbers, self.top_number,
                  self.bottom_number, self.bottom_term, self.to_find_term,
                  self.answer, self.separator]:
            i.set('')

    def widgets(self):
        ttk.Label(self, text='Givens:').grid(column=0, row=0, columnspan=2)
        ttk.Label(self, text='Initial Pressure (P1):').grid(
            column=0, row=1, sticky=E)
        ttk.Entry(self, textvariable=self.p1).grid(column=1, row=1, sticky='WE')
        ttk.Label(self, text='Final Pressure (P2):').grid(
            column=0, row=2, sticky=E)
        ttk.Entry(self, textvariable=self.p2).grid(column=1, row=2, sticky='WE')
        ttk.Label(self, text='Initial Volume (V1):').grid(
            column=0, row=3, sticky=E)
        ttk.Entry(self, textvariable=self.v1).grid(column=1, row=3, sticky='WE')
        ttk.Label(self, text='Final Volume (V2):').grid(
            column=0, row=4, sticky=E)
        ttk.Entry(self, textvariable=self.v2).grid(column=1, row=4, sticky='WE')
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=5, columnspan=2, sticky='WE', pady=10)
        ttk.Button(self, text='Process', command=self.process).grid(
            column=0, row=6, columnspan=2, sticky='WE')
        ttk.Button(self, text='Clear', command=self.clear).grid(
            column=0, row=7, columnspan=2, sticky='WE')
        ttk.Separator(self, orient=HORIZONTAL).grid(
            column=0, row=8, columnspan=2, sticky='WE', pady=10)
        ttk.Label(self, text="Direction:\n"
                             "Leave the field of the missing term\n"
                             "empty or just type '?' in finding it.").grid(
            column=0, row=9, columnspan=2, rowspan=4)
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
        ttk.Label(self, textvariable=self.bottom_number).grid(
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
    app = LawOfBoyleSolver(root)
    app.grid(column=0, row=0, sticky='NEWS')
    text = font.Font(family='Segoe Print', size=11,
                     weight='bold')
    ttk.Style().configure('TFrame', background='lightgreen')
    ttk.Style().configure('TLabel', font=text, background='lightgreen')
    ttk.Style().configure('TButton', font=text, background='lightgreen')
    root.title("Boyle's Law")
    root.mainloop()
