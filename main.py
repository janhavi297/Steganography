from PIL import Image
from binary import convertToBinary

def encodeImage (inputImage, text):
    img = Image.open(inputImage).convert("RGB")
    binaryText = convertToBinary(text)
    width, height = img.size
    
    textIndex = 0
    
    for y in range(height):
        for x in range(width):
            if textIndex < len(binaryText):
                r, g, b = img.getpixel((x, y))
                color = [r,g,b]
                
                for i in range(len(color)):
                    if textIndex < len(binaryText):    
                        bit = int(binaryText[textIndex])
                        color[i] = (color[i] & ~1) | bit
                        textIndex += 1
                img.putpixel(((x, y)), tuple(color))  
                             
            else:
                img.save("output_image.png")
                print("image saved successfully")
                return
            
encodeImage("image2.jpg", "hello ayushi, myself janhavi")