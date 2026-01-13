from decoder import decodeImage
from encoder import encodeImage

print("**************IMAGE STEANOGRAPHGY**************")
option = input("Enter: \n1 to encode\n2 to decode")

if option=="1":
    inputImg = input("Enter the image to be encoded")
    inputText = input("Enter the text to be encoded")
    encodeImage(inputImg, inputText)
    
elif option=="2":
    inputSteg = input("Enter the image to be decoded")
    decodeImage(inputSteg)
    
else:
    print("Invalid response")