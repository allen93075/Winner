import urllib.request as req
import bs4

def webcrawler():
    url = "https://www.ettoday.net/feature/%E8%82%A1%E7%A5%A8/6744?tt=%E8%82%A1%E7%A5%A8%E7%9B%B8%E9%97%9C%E6%96%B0%E8%81%9E"
    # 建立request 物件，發送要求避免被拒絕
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="box_0 clearfix")
    a =[]
    for title in titles:
        if title.h2 != None:
            a.append(title.h2.string)
    return a

webcrawler()





