from PIL import Image
from binary import convertToBinary

def encodeImage (inputImage, text, outputImage):
    img = Image.open(inputImage).convert("RGB")
    binaryText = convertToBinary(text)
    width, height = img.size
    
    binTextIndex = 0
    
    for y in range(height):
        for x in range(width):
            if binTextIndex < len(binaryText):
                r, g, b = img.getpixel((x, y))
                color = [r,g,b]
                
                for i in range(len(color)):
                    if binTextIndex < len(binaryText):    
                        bit = int(binaryText[binTextIndex])
                        color[i] = (color[i] & ~1) | bit
                        binTextIndex += 1
                img.putpixel((x, y), tuple(color))  
                             
            else:
                img.save(outputImage)
                print("image saved successfully")
                return