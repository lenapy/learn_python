import tkinter as t



window = t.Tk()

def convert():
	kg = float(e1_value.get())
	grams = kg * 1000
	pounds = kg * 2.20462
	ounces = kg * 35.274
	t1.insert(t.END, grams)
	t2.insert(t.END, pounds)
	t3.insert(t.END, ounces)

label1 = t.Label(window, text="Kg").grid(row=0, column=1)

b1 = t.Button(window, text='Convert', command=convert).grid(row=0, column=3)

e1_value = t.StringVar()

e1 = t.Entry(window, textvariable=e1_value).grid(row=0, column=2)

t1 = t.Text(window, height=1, width=20)
t1.grid(row=2, column=1)
t2 = t.Text(window, height=1, width=20)
t2.grid(row=2, column=2)
t3 = t.Text(window, height=1, width=20)
t3.grid(row=2, column=3)

window.mainloop()