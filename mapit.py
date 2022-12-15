# import webbrowser , sys
# import pyperclip as pc
# #-------open a browser-------#
# if len(sys.argv) > 1:
#     #Get address from command line
#     address = ''.join(sys.argv[2:])
# else:
#     #Get address from clipboard
#     address =pc.paste()

# webbrowser.open('https://www.google.com/maps/place/' + address)


#------download a web page--------#

import requests as req
import bs4

#res = req.get('https://automatetheboringstuff.com/files/rj.txt')
#res = req.get('https://automatetheboringstuff.com/unexistent_page.html')
res = req.get('https://nostarch.com')
try:
    res.raise_for_status()
    exampleFile = open('example.html')
    exampleSoup =bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
    elements = exampleSoup.select('#author')
    print(str(elements[0].getText()))
    print(str(elements[0].attrs))



except Exception as exc:
    print('There was a problem: %s' % (exc))

""" 
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(type(noStarchSoup))


     playFile = open('RomeoAndJuliet.txt', 'wb') #'wb' write binary mode
    for chunk in res.iter_content(100000):
         playFile.write(chunk)

    playFile.close() 

print(type(res))
print(res.status_code == req.codes.ok)
print(len(res.text))
print(res.text[:75])  """


