## Baidu Novel Scraper

>This is used to scrape books from dushu.baidu.com

- single thread is default in main
- multi-thread can be done using baidunovel.py, run at your own risk.
- async version is in baidunovel_multithread.py

Please use this for learning purpose only.

`pip install -r requirements.txt` 
`python main.py`

1. Search for the book you want to download and package, change the book_id in the main file, you can find the id in the url as gid=? e.g.
https://dushu.baidu.com/pc/detail?gid=4306063500

2. You can find output files in `./data` folder.
