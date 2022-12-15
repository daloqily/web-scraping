import requests, sys,  webbrowser
import bs4


try:
   #res = requests.get('https://pypi.org/search/?q='
   # + ' '.join(sys.argv[1:]))
   
    res = requests.get('https://google.com/search?q='
    + ' '.join(sys.argv[1:]))

    res.raise_for_status()

    # Retrieve top search result links.
    soup = bs4.BeautifulSoup(res.text , 'html.parser')
    #print(str(res.text))
    print('Searching..')

    # Open a browser tab for each result.
    linkElems = soup.select('.b_attribution')
    numOpen = min(5, len(linkElems))
    #print('before loop')
    for i in range(numOpen):
       # print('in loop')
        urlToOpen = 'https://google.com/search' + linkElems[i].get('cite')
        print('Opening', urlToOpen)
        webbrowser.open(urlToOpen)
except Exception as exc:
    print('There was a problem: %s' % (exc))