from bs4 import BeautifulSoup

with open("turing-ugly.html") as file:
	soup = BeautifulSoup(file,'lxml')
	#print(soup.prettify())
	#print(soup.find_all('table')[1].find_all('td'))
	for elem in soup.find_all('table')[1].find_all('td'):
		links = elem.find_all('a')
		if len(links) == 1 :
			if str(links).find('image') != -1 : continue
			if str(links).find('cite') != -1 : continue
			print(links[0].get_text())
