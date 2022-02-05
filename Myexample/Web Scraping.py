# Web scaping means to grab something from a website like a photo

import requests
result = requests.get("https://en.wikipedia.org/wiki/MS_Dhoni")
#print(result.text) # It will print the whole source code of the website we wanted to grab
# It will not be in order, just a string in which all the code is saved

import bs4 #bEAUTIFULsOUP
soup = bs4.BeautifulSoup(result.text,'lxml') # To arrange code
#print(soup) # printing arranged code
print(soup.select('title')) # Grabbing the things from website. Here, we grabbed the title
print(soup.select('title')[0].getText())

# Grabbing a class

class_items = bs4.BeautifulSoup(result.text,'lxml')
# print(class_items)
print(class_items.select(".toctext")[0].getText())
for _ in class_items.select(".toctext"):
    print(_.text)


# Grabbing images and downloading it

image = requests.get("https://en.wikipedia.org/wiki/Alan_Turing")
image_soup = bs4.BeautifulSoup(image.text,'lxml')
#print(image_soup)
turing = image_soup.select(".image")[0]
print(turing)

turing_image = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Alan_Turing_Aged_16.jpg/220px-Alan_Turing_Aged_16.jpg')
f= open("turingImage.jpg",'wb')
f.write(turing_image.content)
f.close()



