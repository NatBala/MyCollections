# loading the required modules
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from wand.image import Image as wandImage
import pytesseract as pyts
pyts.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
from googletrans import Translator
import googletrans
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, TextConverter, XMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io
import hyper
import numpy as np
import pandas as pd
# setting absolute paths
prjPath = r'C:\Users\Natarajan\Desktop\PDFParser'

# # Importing the file and converting it to grayscale
# orgPic = Image.open(os.path.join(prjPath, 'wikipedia.png'))
# grayPic = orgPic.convert('L')
# grayPic = grayPic.point(lambda x: 0 if x < 128 else 255, '1')
# grayPic.save(os.path.join(prjPath, 'wikipediaGrayScale.png'))
#
# # importing the grayscal pic
# grayPic = Image.open(os.path.join(prjPath, 'wikipediaGrayScale.png'))
#
# # converting the image to string
# textFromImage = pyts.image_to_string(grayPic)
# print(textFromImage)

# converting pdf to image using wand
fileToParse = 'SampleRussian3.pdf'
fileName = fileToParse.split('.')[0]
with(wandImage(filename=os.path.join(prjPath, fileToParse),
               resolution=500)) as source:
    images = source.sequence
    pages = len(images)
    print('Number of pages present in the {} is {}'.format(fileToParse, pages))
    for ind in range(pages):
        wandImage(images[ind]).save(filename=os.path.join(
            prjPath, fileName + 'Page' + str(ind) + '.jpeg'))

# importing the grayscal pic
# using google translation
translator = Translator()
with open(os.path.join(prjPath, fileToParse.replace('pdf', 'txt')), 'w') as ParsedFile:
    for ind in range(pages):
        imageFile = Image.open(os.path.join(prjPath, fileName + 'Page' + str(ind) + '.jpeg'))
        parsedText = pyts.image_to_string(imageFile)
        parsedTextToken = parsedText.split()
        textLength = len(parsedTextToken)
        textLenInd = int(np.ceil(textLength) / 5)
        sampleText = list()
        for itr in range(5):
            sampleText.append(' '.join(parsedTextToken[textLenInd * itr:textLenInd * itr + 4]))
        langDetect = translator.detect(sampleText)
        langDict = pd.DataFrame(columns=['Lang', 'Confidence'])
        for lang in langDetect:
            langDict = langDict.append({'Lang': lang.lang,
                                        'Confidence': lang.confidence}, ignore_index=True)
        engToken = np.sum(np.array(langDict['Lang'] == 'en') &
                          np.array(langDict['Confidence'] > 0.75))
        if engToken >= 3:
            engLang = 'Yes'
        else:
            engLang = 'No'
        if engLang == 'No':
            print('Page No {} is Non English and using Google to Translate'.format(ind + 1))
            translatedText = translator.translate(parsedText)
            print('Detected Lang for Page No {} is {}'.format(ind + 1,
                                                              googletrans.LANGUAGES[translatedText.src]))
            ParsedFile.write('PAGE NO. {} \n'.format(ind + 1) + translatedText.text
                             + '\n')
        else:
            ParsedFile.write('PAGE NO. {} \n'.format(ind + 1) + parsedText + '\n')

test = translator.translate("Лорем ипсум долор сит амет, фугит мнесарчум ут сеа, ет цум граеце тамяуам. Хас сумо сенсибус торяуатос цу, десеруиссе витуператорибус еа еос. Ид нец сенсибус ехплицари. Яуодси адмодум менандри яуи ех, сале лобортис еа меи. Еррем мелиус сусципиантур сеа ут, хабемус цонсететур диссентиас пер не.")
print(test)
