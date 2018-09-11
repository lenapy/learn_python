import tkinter as t
from udemy.oop_section.backend import dataBase

db = dataBase('books.db')

class window:
	def __init__(self, window):
		self.selected_tuple = None
		self.window = window
		self.window.wm_title("BookStore")
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
		self.title_text = t.StringVar()
		self.e1 = t.Entry(window, textvariable=self.title_text)
		self.e1.grid(row=0, column=1)

		self.author_text = t.StringVar()
		self.e2 = t.Entry(window, textvariable=self.author_text)
		self.e2.grid(row=0, column=3)

		self.year_text = t.StringVar()
		self.e3 = t.Entry(window, textvariable=self.year_text)
		self.e3.grid(row=1, column=1)

		self.isbn_text = t.StringVar()
		self.e4 = t.Entry(window, textvariable=self.isbn_text)
		self.e4.grid(row=1, column=3)

		# listbox
		self.list1 = t.Listbox(window, height=6, width=35)
		self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

		self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

		# scrollbar
		sb1 = t.Scrollbar(window)
		sb1.grid(row=2, column=2, rowspan=6)

		self.list1.configure(yscrollcommand=sb1.set)
		sb1.configure(command=self.list1.yview)

		# buttons
		b1 = t.Button(window, text="View all", width=12, command=self.view_command)
		b1.grid(row=2, column=3)

		b2 = t.Button(window, text="Search entry", width=12, command=self.search_command)
		b2.grid(row=3, column=3)

		b3 = t.Button(window, text="Add entry", width=12, command=self.add_command)
		b3.grid(row=4, column=3)

		b4 = t.Button(window, text="Update selected", width=12, command=self.update_command)
		b4.grid(row=5, column=3)

		b5 = t.Button(window, text="Delete selected", width=12, command=self.delete_command)
		b5.grid(row=6, column=3)

		b6 = t.Button(window, text="Close", width=12, command=window.destroy)
		b6.grid(row=7, column=3)

	def get_selected_row(self, event):
		index = self.list1.curselection()
		if index:
			index = index[0]
			self.selected_tuple = self.list1.get(index)
			self.e1.delete(0, t.END)
			self.e1.insert(t.END, self.selected_tuple[1])
			self.e2.delete(0, t.END)
			self.e2.insert(t.END, self.selected_tuple[2])
			self.e3.delete(0, t.END)
			self.e3.insert(t.END, self.selected_tuple[3])
			self.e4.delete(0, t.END)
			self.e4.insert(t.END, self.selected_tuple[4])

	def view_command(self):
		self.list1.delete(0, t.END)
		for row in db.view():
			self.list1.insert(t.END, row)

	def search_command(self):
		self.list1.delete(0, t.END)
		for row in db.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
			self.list1.insert(t.END, row)

	def add_command(self):
		db.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
		self.list1.delete(0, t.END)
		self.list1.insert(t.END, (self.title_text.get(), self.author_text.get(),
								  self.year_text.get(), self.isbn_text.get()))

	def delete_command(self):
		db.delete(self.selected_tuple[0])

	def update_command(self):
		db.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(),
				  self.year_text.get(), self.isbn_text.get())

w = t.Tk()
window(w)
w.mainloop()