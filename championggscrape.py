import bs4, requests, time

champ = input('Enter a champion: ')
url = f'https://champion.gg/champion/{champ}/'
rq = requests.get(url)
if str(rq) == '<Response [500]>':
    print('ERROR')
else:
    print(f'Searching for {champ.capitalize()} on {url} ')
    soup = bs4.BeautifulSoup(rq.text, 'html.parser')
    prtty = soup.prettify()
    find = soup.find_all('div' ,class_= 'u-spacing-30')
    