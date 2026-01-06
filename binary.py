def convertToBinary (text):
    text = text + "$$"
    binary = ""
    
    for char in text:
        binary += format(ord(char), '08b')
    
    return binary