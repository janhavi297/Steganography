def convertToBinary (text):
    text = text + "$$"
    binary = ""
    
    for char in text:
        binary += format(ord(char), '08b')
    
    return binary

def convertToText (binary):
    text = ""
    
    while True:
        s = 0
        p = binary[s:s+8]
        text += chr(int(p, 2))
        binary = binary[s+8:]
        
        if len(text)>=2 and text[-2:]=="$$":
            return text[:-2]