'''
A module what gets information about hololive streaming from hololive schedule web page.
'''

from pprint import pprint
import requests
from bs4 import BeautifulSoup

url = "https://schedule.hololive.tv/"

class Stream:
    def __init__(self, owner, timestamp, thumbnail, url):
        self.owner = owner
        self.timestamp = timestamp
        self.thumbnail = thumbnail
        self.url = url
    
    def getInfo(self):
        return (self.owner, self.timestamp, self.thumbnail, self.url)
    
def rawSoup():
    global url
    res = requests.get(url)

    if res.status_code != 200:
        raise("""HoloPush Error
        Connection Failed(""" + res.status_code + ")")

    soup = BeautifulSoup(res.text, 'html.parser')

    if not soup:
        raise("""HoloPush Error
        Connection Failed(""" + "cannot get html" + ")")
    
    return soup

def old_connect():
    ret = []
    soup = rawSoup()

    b = soup.body

    rawInfo = b.find('div', {"id":"all"})

    for info in rawInfo:
        tmp = info.getText().strip().replace("\n", "").replace("\r", "")
        if not tmp:
            continue

        rawData = ' '.join(tmp.split()).split()
        
        for idx in range(len(rawData) // 2):
            ret.append(rawData[2*idx] + " " + rawData[2*idx + 1])
    
    return ret

def old_beautify(scheduleData):
    ret = {}
    recentDate = ""

    for s in scheduleData:
        if s.find('/') >= 0:
            ret[s] = []
            recentDate = s
        else:
            ret[recentDate].append(s)

    return ret

def connect():
    '''
    type : Dict
    key : Date
    value : <class Stream>
    '''
    soup = rawSoup()
    b = soup.body
    ret = {}
    recentDate = ""

    idx1 = 1

    while True:
        idx2 = 1
        while True:
            tmp = b.select("#all > div:nth-child(" + str(idx1) + ") > div > div:nth-child(" + str(idx2) + ") > div")

            if not tmp:
                break

            idx2 += 1

            if tmp[0].find("a"):
                idx3 = 1
                while True:
                    streamInfo = tmp[0].select_one("div:nth-child(" + str(idx3) + ") > a > div > div")

                    if not streamInfo:
                        break

                    idx3 += 1

                    streamTimestamp, streamOwner = ' '.join(streamInfo.getText().strip().replace("\n", "").replace("\r", "").split()).split()
                    streamURL = streamInfo.parent.parent.attrs["href"]
                    streamThumbnail = streamInfo.select_one("div:nth-child(2) > img").attrs["src"]

                    s = Stream(owner=streamOwner, timestamp=streamTimestamp, thumbnail=streamThumbnail, url=streamURL)

                    ret[recentDate].append(s)

            else:
                res = ' '.join(tmp[0].getText().strip().replace("\n", "").replace("\r", "").split())

                if not res:
                    continue

                ret[res] = []
                recentDate = res

        if idx2 == 1:
            break

        idx1 += 1
    
    return ret


if __name__ == '__main__':
    print("Run 'main.py'")
