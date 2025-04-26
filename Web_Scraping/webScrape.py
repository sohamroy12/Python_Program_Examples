import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')

def sort_stories_by_vote(hnlist):
    return sorted(hnlist, key= lambda k:-k['votes'])


def create_hn(l, s):
    hn = []
    for idx, item in enumerate(l):
        title = item.getText()
        url = item.a.get('href', None)
        vote = s[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link' : url, 'votes' : points})
    return sort_stories_by_vote(hn)

pprint.pp(create_hn(links, subtext))


"""
Awesome! 🙌
Glad it clicked. You're doing great diving into real web scraping like this.

If you ever want to go deeper — like sorting, scraping multiple pages, or making it even faster with async — just let me know! 🚀

Happy coding!
"""