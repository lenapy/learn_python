import csv

path = r'C:\Users\Helen\Documents\ingest_files\test.csv'
with open(path) as csvfile:
	m = list(csv.DictReader(csvfile))
	columns = m[0].keys().replace('\t', '')

print(columns)
print(m[:2])

