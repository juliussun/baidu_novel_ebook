import requests
import asyncio
import json
import aiofiles
import aiohttp

""" 
1. get all the novel getCatalog cid name
2. async getChapterContent download content
"""


async def aiodownload(cid, b_id, title):
    data = {"book_id": b_id, "cid": f"{b_id}|{cid}", "need_bookinfo": 1}
    dir = "./data/"
    data = json.dumps(data)
    # Content request url content
    url_content = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url_content) as res:
            dict = res.json()
            async with aiofiles.open((dir + title), mode="w", encoding="utf-8") as f:
                try:
                    print("write: " + title)
                    await f.write(dict["data"]["novel"]["content"])
                except TypeError:
                    print("not subscritpable")

async def getCatelog(url):
    res = requests.get(url)
    dict = res.json()
    tasks = []
    for item in dict["data"]["novel"]["items"]:
        title = item["title"]
        cid = item["cid"]
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    # Chapters request url name, cid
    b_id = "4306063500"
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":' + b_id + "}"
    asyncio.run(getCatelog(url))
