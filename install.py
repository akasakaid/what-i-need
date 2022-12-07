from os import popen, system
from time import sleep
from sys import exit

zenmate = 'https://chrome.google.com/webstore/detail/zenmate-free-vpn%E2%80%93best-vpn/fdcgdnkidjaadafnichfpabhfomcebme?hl=en'
autorefresh = 'https://chrome.google.com/webstore/detail/auto-refresh-plus-page-mo/hgeljhfekpckiiplhkigfehkdpldcggm?hl=en'
hoxxvpn = 'https://chrome.google.com/webstore/detail/hoxx-vpn-proxy/nbcojefnccbanplpoffopkoepjmhgdgh'
useragent = 'https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg'
spooftime = 'https://chrome.google.com/webstore/detail/spoof-timezone/kcabmhnajflfolhelachlflngdbfhboe'
skipads = 'https://chrome.google.com/webstore/detail/youtube-video-skip-ad-tri/hpnelpabemhjfjgiibgkliipaehnfcjk?hl=id'
erase = 'https://chrome.google.com/webstore/detail/hdgnienkeomlaeeojaibeicglpoaadnj'


list_ma_url = ['https://youtu.be/VyGnVrbZXgY', 'https://youtu.be/5Ucr4pcvWME', 'https://youtu.be/vUCy7aohKaU',
               'https://youtu.be/pFLGtsoeXaE', 'https://youtu.be/AJaJWF3IUSA', 'https://youtu.be/sqol483YaUc']


def startup(name, app=None):
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
    print("""
0. start chrome 
1. install zenmate vpn
2. install autorefresh plus
3. install hoxx vpn
4. install user agent switcher
5. install spoofing time
6. install skipper ads
7. install erase data
		""")
    print()
    choice = int(input('-> input number : '))
    if choice == 0:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp)
            sleep(3)
    if choice == 1:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, zenmate)
            sleep(3)
    elif choice == 2:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, autorefresh)
            sleep(3)
    elif choice == 3:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, hoxxvpn)
            sleep(3)
    elif choice == 4:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, useragent)
            sleep(3)
    elif choice == 5:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, spooftime)
            sleep(3)
    elif choice == 6:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, skipads)
            sleep(3)
    elif choice == 7:
        start = int(input('- start : '))
        end = int(input('- end : '))
        for i in range(start, end+1):
            nameapp = 'chrome-' + str(i).zfill(3)
            startup(nameapp, erase)
            sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
