from os import popen,system
from time import sleep

zenmate = 'https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=en'
autorefresh = 'https://chrome.google.com/webstore/detail/auto-refresh-plus-page-mo/hgeljhfekpckiiplhkigfehkdpldcggm?hl=en'

def startup(name,app):
	command = 'start ' + name + ' ' + app
	res = popen(command)
	return

def main():
	system('cls')
	print('- menu ')
	print('1. install zenmate')
	print('2. install auto refresh ')
	print()
	choice = int(input('-> input number : '))
	if choice == 1:
		start = int(input('- start : '))
		end = int(input('- end : '))
		for i in range(start,end+1):
			nameapp = 'chrome-' + str(i).zfill(3)
			startup(nameapp,zenmate)
	elif choice == 2:
		start = int(input('- start : '))
		end = int(input('- end : '))
		for i in range(start,end+1):
			nameapp = 'chrome-' + str(i).zfill(3)
			startup(nameapp,autorefresh)
