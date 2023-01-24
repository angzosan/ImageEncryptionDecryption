import io
from PIL import Image
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def encr_decry(Cipher,key):
  arr = [ 0 for i in range(0, len(Cipher))]
  for i in range(0, len(Cipher)):
      arr[i] = Cipher[i]^key
  return arr


#path = input("Enter the path of the image for encryption : ")
key = input( "Enter they key for the encryption : ")
key = int(key) 
path = 'image.jpg'

with open(path, "rb") as image:
  f = image.read()
  imagByt = bytearray(f)

encryImage = encr_decry(imagByt,key)
encryImage = bytearray(encryImage)
print('The image has been encrypted.')
#print(encryImage)

print("Decryption process begins... ")

decryImage = encr_decry(encryImage,key)
print('The image has been decrypted.')
#print(decryImage)
