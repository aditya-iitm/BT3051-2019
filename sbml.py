from bs4 import BeautifulSoup

with open("turing-ugly.html") as file:
	soup = BeautifulSoup(file,'lxml')
	#print(soup.prettify())
	for elem in soup.find_all('table')[1].find_all('td'):
		link = elem.find_all('a')
		for item in link:
			title = item['title']