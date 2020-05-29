import requests
from bs4 import BeautifulSoup
import datetime
import os
import sys


def padzero(i):
    need_len = 2
    length = len(str(i))
    return "0"*(need_len-length) + str(i)


from_date = datetime.date(2020, 5, 29)
delta = datetime.timedelta(days=1)
to_date = datetime.date(2020, 5, 29)

counter = 0
total = 0

while from_date <= to_date:
    year = from_date.year
    month = from_date.month
    day = from_date.day
    for i in range(1, int(1e4)):
        url = "http://stihi.ru/{}/{}/{}/{}".format(year, padzero(month), padzero(day), i)
        try:
            r = requests.get(url)

            soup = BeautifulSoup(r.text, features="lxml")
            author = soup.find('div', {'class': 'titleauthor'}).text
            title = soup.find("h1").text
            text = soup.find('div', {'class': 'text'}).text

            if not os.path.exists("./poems/{}/{}.txt".format(author, title)):
                os.makedirs("./poems/{}/".format(author, title))

            open("./poems/{}/{}.txt".format(author, title), 'w', encoding='utf8').write(text + "\n\n" + str(from_date))
            flag = "SUCCESS"
            counter += 1
        except:
            flag = "ERROR"
            continue
        finally:
            total += 1
            os.system("cls")
            sys.stdout.write("\r{}/{} {:.2f}% successful, now PROCESSING {} : {}"
                             .format(counter, total, counter*100.0/total, url, flag))
            sys.stdout.flush()
    from_date += delta

