from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def StartSearch():
    search = input("Enter search term: ")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()
    if not os.path.idDir(dir_name):
        os.mkdir(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})
    for items in links:
        img_obj = requests.get(items.attrs["href"])
        print("Getting", items.attrs["href"])
        title = items.attrs["href"].split("/")[-1]
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./images/" + title, img.format)
        except:
            print("Could not save image")


StartSearch()
