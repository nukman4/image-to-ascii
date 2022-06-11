import Image
density = "Ñ@#W$9876543210?!abc;:+=-,._ ";
pic = ""
try: 
    img  = Image.open("image.png") #replace image.png with desired images path
except IOError:
    print("not working")
    pass
def findchar(x,end1,end2):
  d = end1 / end2
  x = x/d
  x=int(x)
  return x

img = img.resize((64,32)) #replace 64 and 32 with desired dimensions
img = img.convert("RGB")
pixel_map = img.load()
h, w = img.size
for i in range(w):
  for j in range(h):
    r, g, b = img.getpixel((j, i))
    avg = (0.299*r + 0.587*g + 0.114*b)
    leng = len(density)
    pos = findchar(avg,255,leng)
    pic+=density[pos]
  pic+="\n"
print(pic)
