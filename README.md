# ．網路爬蟲WebCrawler_hw
# ．crawler1爬的邏輯為進入一篇TVBS新聞，解析html並抓取五項資料:標題、url、記者、時間、內文，並在相關新聞繼續爬取下一篇新聞，直到相關新聞皆已拜訪過或達到爬取數量停止。由於TVBS一篇新聞底下的相關新聞數目有限(相關只有秀出10篇)，此方法可能在爬了5、600篇後，相關新聞就都是已拜訪過而停止繼續爬。
# ．crawler2使用selenium先捲動至底部已獲取更多篇新聞，捲動完畢後逐一拜訪各篇新聞並抓取五項資料:標題、url、記者、時間、內文。
