import requests
import json
from concurrent.futures import ThreadPoolExecutor

def download(cid, book_id, title):
    data = {
        "book_id":book_id,
        "cid":f"{book_id}|{cid}",
        "need_bookinfo":1
    }
    dir = "./data/" # data output dir
    data = json.dumps(data)
    url_content = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    res = requests.get(url_content)
    dict = res.json()
    with open((dir+title+".txt"),mode='w', encoding='utf-8') as f:
        f.write(dict['data']['novel']['content'])

def getCatalog(url):
    res = requests.get(url)
    dict = res.json()
    # using threadpool of size 25
    with ThreadPoolExecutor(25) as t:
        for item in dict["data"]["novel"]["items"]:
            title = item["title"]
            cid = item["cid"]
            t.submit(download(cid,book_id,title))

if __name__ == "__main__":
    # Chapters request url name, cid
    book_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":'+book_id+'}'
    getCatalog(url)