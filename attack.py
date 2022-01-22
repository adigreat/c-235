import requests
for i in range (1,100):
    url=f"  http://www.mybarkerhome.com/news_view.php?id='8{i}"
    r=requests.get(url=url)
    if r.status_code==200:
        print(url)
    