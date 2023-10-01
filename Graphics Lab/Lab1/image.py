import turtle
from PIL import Image
image_path_jpg = './tomjerry.jpg'
image_path_gif = './tomjerry.gif'
img = Image.open(image_path_jpg)
img.save(image_path_gif, 'GIF')

turtle.bgpic(image_path_gif)
turtle.exitonclick()
