# Steganography
## About the project
Image Steganography is a method of hiding secret data or messages by embedding it into image. In the context of digital images, LSB (Least Significant Bit) Steganography is one of the technique to hide secret data in it.

## Features
- Encodes secret text in the image
- Decodes secret text from the image
- Uses LSB Steganography technique
- Terminator based secret text detection

## How does it works?
### Encoder
The secret text is taken input from the user in the form of string. The is then converted in a binary string containing the binary encoding of the ascii value of each character. Each character is stored as 8 bits (1 byte). The terminator "$$" is added to mark the end of the text. Each bit of the binary string is the stored at LSB of the image pixels one by one. Changing the LSB does not significantly changes the image.

### Decoder
The LBS of each pixel is read and the binary string is generated. This string is then decoded and the secret text is reveled. 

## Tech Stack
- Python
- Pillow library

##### Note: Storing the steganographic image in .png instead of .jpg provides better result.

