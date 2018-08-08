import tkinter as t

window = t.Tk()

def km_to_miles():
	miles = float(e1_value.get())*1.6
	t1.insert(t.END, miles)



b1 = t.Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0)

e1_value = t.StringVar()
e1 = t.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = t.Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()


