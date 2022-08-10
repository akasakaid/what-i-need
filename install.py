from os import popen,system
from time import sleep
from sys import exit

zenmate = 'https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=en'
autorefresh = 'https://chrome.google.com/webstore/detail/auto-refresh-plus-page-mo/hgeljhfekpckiiplhkigfehkdpldcggm?hl=en'
list_ma_url = ['https://youtu.be/VyGnVrbZXgY','https://youtu.be/5Ucr4pcvWME','https://youtu.be/vUCy7aohKaU','https://youtu.be/pFLGtsoeXaE','https://youtu.be/AJaJWF3IUSA','https://youtu.be/sqol483YaUc']

def startup(name,app=None):
	if app:
		command = 'start ' + name + ' ' + app
		res = popen(command)
		return
	else:
		command = 'start ' + name + ' '
		res = popen(command)
		return

def main():
	system('cls')
	print('- menu ')
	print('0. start all chrome')
	print('1. install zenmate')
	print('2. install auto refresh ')
	print()
	choice = int(input('-> input number : '))
	if choice == 0:
		start = int(input('- start : '))
		end = int(input('- end : '))
		for i in range(start,end+1):
			nameapp = 'chrome-' + str(i).zfill(3)
			startup(nameapp)
			sleep(5)
	if choice == 1:
		start = int(input('- start : '))
		end = int(input('- end : '))
		for i in range(start,end+1):
			nameapp = 'chrome-' + str(i).zfill(3)
			startup(nameapp,zenmate)
			sleep(5)
	elif choice == 2:
		start = int(input('- start : '))
		end = int(input('- end : '))
		for i in range(start,end+1):
			nameapp = 'chrome-' + str(i).zfill(3)
			startup(nameapp,autorefresh)
			sleep(5)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
