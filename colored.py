from PIL import Image
import urllib.request
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)
  
print(colored(255, 0, 0, 'Hello, World'))
pic = ""
pic1 =""
url = input("image url: ")
choice = input("[1]JPG  [2]PNG ")
if choice == "2":
  urllib.request.urlretrieve(url, "image.jpg")
  try: 
      img  = Image.open("image.jpg") 
  except IOError:
      print("not working")
      pass
if choice == "1":
  urllib.request.urlretrieve(url, "image.png")
  try: 
      img  = Image.open("image.png") 
  except IOError:
      print("not working")
      pass
x = int(input("width: "))
y = int(input("height: "))
img = img.resize((x*2,y))
img = img.convert("RGB")
pixel_map = img.load()
h, w = img.size
for i in range(w):
  for j in range(h):
    r, g, b = img.getpixel((j, i))
    avg = int((0.299*r + 0.587*g + 0.114*b))
    text = '0'
    colored_text = colored(avg, avg, avg, text)
    pic += colored_text
    text = '0'
    colored_text = colored(r, g, b, text)
    pic1+=colored_text
  pic += "\n"
  pic1 +="\n"
#print(pic)
print(pic1)
