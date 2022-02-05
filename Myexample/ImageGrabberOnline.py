import requests
website_content = requests.get("https://en.wikipedia.org/wiki/MS_Dhoni")
import bs4
website_soup = bs4.BeautifulSoup(website_content.text,"lxml")
#print(website_soup)
image_grab = website_soup.select(".infobox-image")[0]
#print(image_grab)
get_image = requests.get('https://upload.wikimedia.org/wikipedia/commons/7/70/Mahendra_Singh_Dhoni_January_2016_%28cropped%29.jpg')
f= open("dhoni_image.jpg",'wb')
f.write(get_image.content)
f.close()
