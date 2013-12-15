import urllib2
from bs4 import BeautifulSoup

def find_times_and_urls():
    url = 'http://www.sporcle.com/games/'

    conn = urllib2.urlopen(url)
    html = conn.read()

    soup = BeautifulSoup(html)
    links = soup.find_all('a')

    allLinks = list()

    for tag in links:
        allLinks.append((tag.get('href')))
    
    games=[link for link in allLinks if "games/" in link]
        
    final_games =[link for link in games if games if "games/category/" not in link]
    final_games =[link for link in final_games if final_games if "games/contributed" not in link]
    final_games =[link for link in final_games if final_games if "games/g/" not in link]
    final_games = [link for link in final_games if final_games if ".php" not in link]
    
    for a in range(len(final_games)):
        final_games[a]= 'http://www.sporcle.com' + final_games[a]
        
    url_for_times = []
    for a in range(len(final_games)):
        conn = urllib2.urlopen(final_games[a])
        html = conn.read()
        soup = BeautifulSoup(html)
        links = soup.find(id="time")
        url_for_times.append(links)
    url_times = zip(final_games, url_for_times)
    return url_times

def parse times_and_urls(url_times):
    regex = re.compile("\">(?P<time>\d\d\:\d\d)")
    times = [regex.findall(i[1])[0] for i in url_times]    
    times = [time[0] for time in times]
    urls = [i[0] for i in url_times]
    print times
    # try to get this shit in the right format like you can see my other work
    

