import urllib.request as req
count=10

def getData(url):
    request=req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")

    
    print("網址: ")
    print(url)

    print("標題: ")
    titles=root.find("h1",class_="title")
    if titles!=None:
        print(titles.string)

    print("記者: ")
    author=root.find("div",class_="author")
    if author.a!=None:
        print(author.a.string)

    time=root.find("div",class_="author").find_all("br")
    print("時間: ")
    if time!=None:
        for con in time:
            if con.string!=None:
                print(con.string)

    print("內文: ")
    content=root.find("div",class_="article_content")
    if content!=None:
        
        print(content.get_text())

    #回傳下篇連結
    nexturl=root.find("h2",class_="txt")
    if nexturl!=None:
        if nexturl.a!=None:
            nexturl="https://news.tvbs.com.tw"+nexturl.a["href"]
            return nexturl
    


url="https://news.tvbs.com.tw/world/2111412?from=life_extend"
ind = 0
while ind<count:
    print("第"+str(ind+1)+"篇")
    url=getData(url)
    print("\n-------------------------------next--------------------------------")
    ind+=1 
