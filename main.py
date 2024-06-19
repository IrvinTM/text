from PIL import ImageGrab, Image
import os
import pyperclip

os.system('grim -g "$(slurp)" - | swappy -f -')

img = ImageGrab.grabclipboard()

img.save('image.png')

# Run Tesseract OCR and capture the output
result = os.popen('tesseract image.png stdout -l spa').read()

pyperclip.copy(result)


os.system('notify-send --expire-time=2000 "Text copied to clip"')


