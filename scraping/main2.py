import requests
from bs4 import BeautifulSoup
import os
import sys
import datetime

start = datetime.date(2020, 5, 1)
end = datetime.date(2020, 5, 2)
diff = datetime.timedelta(days=1)

total_reqs = (end - start).days * 10000


success_counter = 0
total = 0


def padzero(i):
    need = 2
    length = len(str(i))
    return "0"*(need - length) + str(i)


while start <= end:
    year = start.year
    month = start.month
    day = start.day

    for i in range(1, 10000):
        try:
            url = "https://stihi.ru/{}/{}/{}/{}".format(year, padzero(month), padzero(day), i)

            text = requests.get(url).text

            # Beautiful Soup
            soup = BeautifulSoup(text, features="lxml")

            title = soup.find('h1').text
            author = soup.find('div', {"class": "titleauthor"}).text
            text = soup.find('div', {"class": "text"}).text

            if not os.path.exists("./poems/{}/".format(author)):
                os.makedirs("./poems/{}/".format(author))
            path = "./poems/{}/{}.txt".format(author, title)
            open(path, "w", encoding="UTF8").write(text)
            success_counter += 1
        except:
            continue
        finally:
            total += 1
            sys.stdout.write(
                "\r{}/{} {:.2f}% successful {:.2f}% done"
                    .format(success_counter, total, success_counter * 100.0 / total, total*100.0/total_reqs))
            sys.stdout.flush()

    start += diff





