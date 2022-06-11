#to put an image right click the desired image from google and click copy image address. not all images work so if you get an error try a different one or check you used the right file extension
import Image
import urllib.request
density = "#$PX0wocv:+!~*. ";
#density = "   .'1780'" #density if you want to print in real paper
#density = "0871|;:'. "
#density = "01 "
pic = ""
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
    
def findchar(x,end1,end2):
  d = end1 / end2
  x = x/d
  x=int(x)
  return x
x = int(input("width: "))
y = int(input("height: "))
img = img.resize((x*2,y))
img = img.convert("RGB")
pixel_map = img.load()
h, w = img.size
for i in range(w):
  for j in range(h):
    r, g, b = img.getpixel((j, i))
    avg = (0.299*r + 0.587*g + 0.114*b)
    leng = len(density)
    pos = findchar(avg,255,leng)
    pic+=density[pos-1]
  pic+="\n"
print(pic)
