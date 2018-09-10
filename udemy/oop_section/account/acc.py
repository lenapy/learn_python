class account:
	def __init__(self, file_path):
		self.file_path = file_path
		with open(self.file_path, 'r') as file:
			self.balance = int(file.read())

	def withdraw(self, amount):
		self.balance = self.balance - amount

	def deposit(self, amount):
		self.balance = self.balance + amount

	def commit(self):
		with open(self.file_path, 'w') as file:
			file.write(str(self.balance))


class checking(account):
	def __init__(self, file_path, fee):
		account.__init__(self, file_path)
		self.fee = fee

	def transfer(self, amount):
		self.balance = self.balance - amount - self.fee

# acc = account(r"C:\Users\Helen\PycharmProjects\learn_python\udemy\oop_section\account\balance.txt")
# print(acc.balance)
# acc.withdraw(100)
# acc.commit()
# print(acc.balance)
# acc.deposit(200)
# acc.commit()
# print(acc.balance)

ch = checking(r"C:\Users\Helen\PycharmProjects\learn_python\udemy\oop_section\account\balance.txt", 1)
ch.transfer(110)
print(ch.balance)
ch.commit()
print(ch.balance)
