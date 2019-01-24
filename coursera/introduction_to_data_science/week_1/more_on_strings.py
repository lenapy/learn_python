"""In Python 3 strings are Unicode based
The Unicode Transformation Format, or UTF, is an attempt to solve this.
It can be used to represent over a million different characters.
This includes not only human languages like you might expect, but symbols like emojis too. """

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

