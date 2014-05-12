__author__ = 'user'

import csv
path = "C:/Users/user/Documents/NYU/FCS/sephora/"



dataDistro =  open(path+"product.csv")

f = csv.DictReader(dataDistro, delimiter=",")
product = []
for row in f:

    product.append((row['product'], float(row['avgrating'])))




dataDistro =  open(path+"reviews.csv")

g = csv.DictReader(dataDistro, delimiter=",")
review = []

for row in g:
    if row[' rating'] == 'null':
        review.append((row['Review Id'], row[' Customer Id'], row[' Badge'], row[' Location'], row[' Skin Type'], row[' Skin Tone'], row[' Eye Color'], row[' Age'], row[' rating'], row[' Title'], row[' Date'], row[' Helpful Votes'], row[' Total Votes']))

    elif row[' rating'].isdigit() == True:
        review.append((row['Review Id'], row[' Customer Id'], row[' Badge'], row[' Location'], row[' Skin Type'], row[' Skin Tone'], row[' Eye Color'], row[' Age'], float(row[' rating']), row[' Title'], row[' Date'], row[' Helpful Votes'], row[' Total Votes']))




dataDistro =  open(path+"productHasReviews.csv")

h = csv.DictReader(dataDistro, delimiter=",")
productHasReview = []
for row in h:

    productHasReview.append(( row['productId'], row['review Id']))




import tkinter as tk
from tkinter import ttk


def quit():
    root.destroy()



def about():
    win=tk.Toplevel(root)
    def ok():
        win.destroy()
    win.title("About")
    win.geometry('200x100-5+40')
    ttk.Label(win,text="Your Best Beauty Product Finder").grid(column=0,row=0)
    button=ttk.Button(win,text="ok",command=ok)
    for child in win.winfo_children():
        child.grid_configure(padx=5, pady=5)
    button.focus()
    win.grab_set()
    root.wait_window(win)


from operator import itemgetter
def best_finder(*args):
    try:
        value = str(skintype_var.get())
        age=str(symbol_var.get())

        ages = ('Null','18-24','25-34','35-44','45-54')
        cindex=ages.index(age)
        skintypes = ('Null','Normal','Oily','Combination','Dry')
        sindex=skintypes.index(value)
        L = [z for z in product if z[0] in [y[0] for y in productHasReview if y[1] in [x[0] for x in review if x[4]==skintypes[sindex] and x[7]==ages[cindex]]]]
        List = sorted(L, key=itemgetter(1), reverse=True)
        bestproduct.set(List[0][0])
        result_string=" Best Product for you is at: www.sephora.com/"
        result_text_value.set(result_string)
    except ValueError:
        pass



root=tk.Tk()
root.title("Beauty Finder")


root.option_add('*tearOff', False)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar)
help_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File",menu=file_menu)
menu_bar.add_cascade(label="Help",menu=help_menu)


file_menu.add_command(label="Exit",command=quit)
help_menu.add_command(label="About",command=about)


root.config(menu=menu_bar)

mainframe = ttk.Frame(root, padding="3 3 12 12")

mainframe.grid(column=0, row=0,sticky=(tk.N, tk.W, tk.E, tk.S))


mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


skintype_var = tk.StringVar()
bestproduct = tk.StringVar()
symbol_var = tk.StringVar()
result_text_value = tk.StringVar()

skintype=ttk.Combobox(mainframe,textvariable=skintype_var)
skintype['values']=('etc','Normal','Oily','Combination','Dry')


symbol=ttk.Combobox(mainframe,textvariable=symbol_var)
symbol['values']=('etc','18-24','25-34','35-44','45-54')


ttk.Label(mainframe, text="Choose your SKIN TYPE and AGE").grid(column=0, row=1, sticky=tk.W)
result_text_label=ttk.Label(mainframe)
result_text_label.grid(column=0,row=2,sticky=tk.W)
result_text_label['textvariable'] = result_text_value
result_text_value.set('')



ttk.Label(mainframe, textvariable=bestproduct).grid(column=1, row=2, sticky=(tk.W, tk.E))


ttk.Button(mainframe, text="Find", command=best_finder).grid(column=3, row=3, sticky=tk.W)






for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
root.bind('<Return>', best_finder)

root.mainloop()