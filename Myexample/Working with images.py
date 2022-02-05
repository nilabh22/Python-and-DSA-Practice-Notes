from PIL import Image, ImageDraw, ImageFilter
image1= Image.open('jpg1.jpg')
#image1.show() # Open up the image

# Cropping our images
print(image1.size)
x= 0 # (x,y) = (0,0) shows we have to crop from top left corner
y= 0
w = 4224 * (2/3)
h = 3136 /4
cropped_image = image1.crop((x,y,w,h))
#cropped_image.show()
image1.paste(im = cropped_image, box = (0,0)) #This will paste the cropped image in image 1 in memory. Original image will not be affected by this.
#image1.show()

# Resizing an image

resize =image1.resize((200,150))
#resize.show()

# Rotating Images

rotate = image1.rotate(90)
#rotate.show()

# RGBA Concept - It gives transparency from 0 to 255 scale to an image

blue = Image.open('bluejpg.jpg')
blue.putalpha(128)

#print(red.size)
#new_red = red.resize(227,100)
#new_red.show()


pink = Image.open('pinkjpg.jpg')
pink.putalpha(128)
#print(blue.size)
#blue.show()

blue.paste(im = pink, box =(0,0), mask = pink)
blue.show()
purple = blue.convert('RGB') # To save we have to convert it first to Mode RGB from jpeg
purple.save('purple.jpg')