from decoder import decodeImage
from encoder import encodeImage

print("**************IMAGE STEANOGRAPHGY**************")
option = input("Enter (1) to encode (2) to decode : ")

if option=="1":
    inputImg = input("Enter the image to be encoded : ")
    inputText = input("Enter the text to be encoded : ")
    outputImg = input("Output Image to be saved as : ")
    encodeImage(inputImg, inputText, outputImg)
    
elif option=="2":
    inputSteg = input("Enter the image to be decoded : ")
    decodeImage(inputSteg)
    
else:
    print("Invalid response")