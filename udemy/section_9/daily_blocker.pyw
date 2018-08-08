import time
from datetime import datetime as dt

hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
hosts_temp = 'hosts'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com']

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, 11) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
		with open(hosts_path, 'r+') as f:
			content = f.read()
			for website in website_list:
				if website in content:
					pass
				else:
					row = '\n{redirect} {website}'.format(redirect=redirect, website=website)
					f.write(row)
	else:
		with open(hosts_path, 'r+') as f:
			content=f.readlines()
			f.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					f.write(line)
			f.truncate()
	time.sleep(5)