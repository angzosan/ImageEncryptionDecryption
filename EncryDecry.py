import io
from PIL import Image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


#path = input("Enter the path of the image for encryption : ")
key = input( "Enter they key for the encryption : ")
key = int(key) 
path = 'image.jpg'

with open(path, "rb") as image:
  f = image.read()
  imagByt = bytearray(f)

#print(imagByt)
encryImage = [ 0 for i in range(0, len(imagByt))]
for i in range(0, len(imagByt)):
    encryImage[i] = imagByt[i]^key

#print(encryImage)
encryImage = bytearray(encryImage)
#imag = Image.frombuffer('L', , encryImage, 'raw', 'L', 0, 1)
#img.show()
#encryImage = bytearray(encryImage)


print('The image has been encrypted.')
print(encryImage)


print("Decryption process begins : ")
decryImage = [ 0 for i in range(0, len(encryImage))]
for i in range(0, len(imagByt)):
    decryImage[i] = encryImage[i]^key


print('The image has been decrypted.')
print(decryImage)
