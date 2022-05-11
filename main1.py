import PyPDF2
import pyttsx3
book = open('html_tutorial (1).pdf' ,'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)

speaker = pyttsx3.init()
page = pdfreader.getPage(7)
text = page.extractText()
speaker.say('text')
speaker.runAndWait()
print('thanks')