import tkinter as t
from udemy.oop_section.backend import dataBase

db = dataBase('books.db')

class helpers:
	def __init__(self):
		self.selected_tuple = None

	def get_selected_row(self, event):
		index = list1.curselection()
		if index:
			index = index[0]
			self.selected_tuple = list1.get(index)
			e1.delete(0, t.END)
			e1.insert(t.END, self.selected_tuple[1])
			e2.delete(0, t.END)
			e2.insert(t.END, self.selected_tuple[2])
			e3.delete(0, t.END)
			e3.insert(t.END, self.selected_tuple[3])
			e4.delete(0, t.END)
			e4.insert(t.END, self.selected_tuple[4])


	def view_command(self):
		list1.delete(0, t.END)
		for row in db.view():
			list1.insert(t.END, row)

	def search_command(self):
		list1.delete(0, t.END)
		for row in db.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
			list1.insert(t.END, row)

	def add_command(self):
		db.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
		list1.delete(0, t.END)
		list1.insert(t.END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

	def delete_command(self):
		db.delete(self.selected_tuple[0])

	def update_command(self):
		db.update(self.selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = t.Tk()
window.wm_title("BookStore")
h = helpers()

# labels
l1 = t.Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = t.Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = t.Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = t.Label(window, text='ISBN')
l4.grid(row=1, column=2)

# entries
title_text = t.StringVar()
e1 = t.Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = t.StringVar()
e2 = t.Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = t.StringVar()
e3 = t.Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = t.StringVar()
e4 = t.Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

# listbox
list1 = t.Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

list1.bind('<<ListboxSelect>>', h.get_selected_row)

# scrollbar
sb1 = t.Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# buttons
b1 = t.Button(window, text="View all", width=12, command=h.view_command)
b1.grid(row=2, column=3)

b2 = t.Button(window, text="Search entry", width=12, command=h.search_command)
b2.grid(row=3, column=3)

b3 = t.Button(window, text="Add entry", width=12, command=h.add_command)
b3.grid(row=4, column=3)

b4 = t.Button(window, text="Update selected", width=12, command=h.update_command)
b4.grid(row=5, column=3)

b5 = t.Button(window, text="Delete selected", width=12, command=h.delete_command)
b5.grid(row=6, column=3)

b6 = t.Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()