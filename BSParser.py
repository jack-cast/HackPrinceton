from bs4 import BeautifulSoup
import urllib.request

# print('All Paths Lead to Philosophy')
# print('')
# print('By starting with a random page on Wikipedia, if you successively follow the first link on each page, you will end up on the Philosophy page in 98' + str('%') + ' of cases!')
# print('')
def wiki(page):
	path = []
	# page = str(input('Enter the title of a valid Wikipedia page and find your path to Philosophy:'))
	print('')
	html_doc = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + page)

	while page != 'Philosophy' and not(page in path):

		path += [page]

		soup = BeautifulSoup(html_doc, 'html.parser')
		string = soup.prettify()
		index = string.find('<p>')
		new_soup = string[index:]

		left_bound = new_soup.find('<a')
		right_bound = new_soup.find('</a>')
		sub_soup = new_soup[left_bound:right_bound]
		new_index = sub_soup.find('>') + 9

		left_check = sub_soup.find('=') + 2
		right_check = left_check + 6
		is_wiki = sub_soup[left_check:right_check]

		while sub_soup[new_index].isupper() or is_wiki != '/wiki/' or sub_soup[right_check:right_check + 4] == 'Help' or \
		 sub_soup[right_check:right_check + 4] == 'File' or sub_soup[right_check:right_check + 9] == 'Wikipedia' or \
		  sub_soup[right_check:right_check + 8] == 'Template' or sub_soup[right_check:right_check + 8] == 'Category':

			left_bound = new_soup.find('<a', left_bound + 1)
			right_bound = new_soup.find('</a>', right_bound + 1)
			sub_soup = new_soup[left_bound:right_bound]
			new_index = sub_soup.find('>') + 9

			left_check = sub_soup.find('=') + 2
			right_check = left_check + 6
			is_wiki = sub_soup[left_check:right_check]

		next_start = sub_soup.find('=') + 8
		next_end = sub_soup.find('"', next_start)
		page = sub_soup[next_start:next_end]
		html_doc = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + page)

	i = 0
	while i < len(path):
		new_word = ''
		x = 0
		while x < len(path[i]):
			if path[i][x] == '_':
				new_word += ' '
				x += 1
			elif path[i][x] == '%':
				a = 1
				while path[i][x+a].isnumeric():
					o = path[i][x:x+a+1]
					a += 1
				if a == 1:
					new_word += '%'
				else:
					new_word += urllib.request.unquote(o)
				x += a
			else:
				new_word += path[i][x]
				x += 1
		path[i] = new_word
		i += 1
	if  page == 'Philosophy':
		path += [page]
		return 'Success! Your path was: ' + str(path)
	else:
		return 'Your page does not lead to Philosophy because it gets caught in the following loop: ' + str(path)

if __name__ == "__main__":
	print(wiki("bottle"))