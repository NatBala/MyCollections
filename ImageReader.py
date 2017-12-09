# loading the required modules
from PIL import Image
import pytesseract as pyts
pyts.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
# Importing the file and converting it to grayscale
orgPic = Image.open(r'C:\Users\Natarajan\Desktop\PDFParser\wikipedia.png')
grayPic = orgPic.convert('L')
grayPic = grayPic.point(lambda x: 0 if x < 128 else 255, '1')
grayPic.save(r'C:\Users\Natarajan\Desktop\PDFParser\wikipediaGrayScale.png')

# importing the grayscal pic
grayPic = Image.open(r'C:\Users\Natarajan\Desktop\PDFParser\wikipediaGrayScale.png')

# converting the image to string
textFromImage = pyts.image_to_string(orgPic)
print(textFromImage)
