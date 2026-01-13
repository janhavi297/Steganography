from PIL import Image
from binary import *

def decodeImage (stegImage):
    img = Image.open(stegImage).convert("RGB")
    width, height = img.size
    binaryText = ""
    lastTwoInBin = convertToBinary("$$")
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x,y))
            color = [r, g, b]
        
            for i in range(len(color)):
                lastBit = str(color[i] & 1)
                binaryText += lastBit
                
                if lastTwoInBin in binaryText:
                    return convertToText(binaryText)
