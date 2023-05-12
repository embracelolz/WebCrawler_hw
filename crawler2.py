import urllib.request as req
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time

def getNewsData(url):
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



options = Options()
options.chrome_executable_path = "D:\PythonWork\PyPrac1\chromedriver.exe"
driver=webdriver.Chrome(options=options)
driver.get("https://news.tvbs.com.tw")
print("=========================================此輪開始=============================================")
index =0
showIndex=0
scrollCount=366
visitCount=10000

while index < scrollCount: # 捲動至底部已獲取更多篇新聞
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(0.5)
    print("捲動"+str(index+1)+"次")
    index+=1
    
print("=======開始拜訪=======")
titelTags=driver.find_element(By.CLASS_NAME,"breaking_news_other_mo")
heading = titelTags.find_elements(By.TAG_NAME,"a")
for titleTag in heading:
    if showIndex>=visitCount:
        print("=======結束拜訪=======")
        break
    else:
        print("第"+str(showIndex+1)+"篇")
        getNewsData(titleTag.get_attribute("href"))
        showIndex+=1
        