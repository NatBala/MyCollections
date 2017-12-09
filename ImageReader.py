# loading the required modules
import os
dir(os)
from PIL import Image
from wand.image import Image as wandImage
import pytesseract as pyts
pyts.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

# setting absolute paths
prjPath = r'C:\Users\Natarajan\Desktop\PDFParser'

# Importing the file and converting it to grayscale
orgPic = Image.open(os.path.join(prjPath, 'wikipedia.png'))
grayPic = orgPic.convert('L')
grayPic = grayPic.point(lambda x: 0 if x < 128 else 255, '1')
grayPic.save(os.path.join(prjPath, 'wikipediaGrayScale.png'))

# importing the grayscal pic
grayPic = Image.open(os.path.join(prjPath, 'wikipediaGrayScale.png'))

# converting the image to string
textFromImage = pyts.image_to_string(grayPic)
print(textFromImage)

# converting pdf to image using wand
with(wandImage(filename=os.path.join(prjPath, 'ScannedFile3.pdf'), resolution=200)) as source:
    images = source.sequence
    pages = len(images)
    for i in range(pages):
        wandImage(images[i]).save(filename=os.path.join(
            prjPath, 'ScannedFile3Page' + str(i) + '.png'))

# importing the grayscal pic
grayPic = Image.open(os.path.join(prjPath, 'ScannedFile3Page0' + '.png'))

# converting the image to string
textFromImage = pyts.image_to_string(grayPic)
print(textFromImage)
