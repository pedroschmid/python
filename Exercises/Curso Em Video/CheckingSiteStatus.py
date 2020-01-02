import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[0;31mThe site "PUDIM" is not currently accessible.\033[m')
else:
    print('I was able to successfully access the site!')        