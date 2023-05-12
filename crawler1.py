import urllib.request as req
count = 1        # 拜訪幾篇新聞
visitedList = [] # 紀錄拜訪過網址，取得下篇相關新聞會檢查是否已拜訪過
def getNewsData(url):
    visitedList.append(url)
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
    nexturl=root.find_all("h2",class_="txt")
    for content in nexturl:
        if (content!=None):
            if (content.a!=None):
                    content="https://news.tvbs.com.tw"+content.a["href"]
                    if(content not in visitedList):
                        return content
    else:
        print("#######################相關新聞皆已拜訪過#######################")
        return "none"
    
url="https://news.tvbs.com.tw/world/2111412?from=life_extend"
index = 0
while index<count:
    print("第"+str(index+1)+"篇")
    url=getNewsData(url)
    if(url!="none"):
        print("\n-------------------------------next--------------------------------")
        index+=1 
    else:
        break
