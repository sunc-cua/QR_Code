#  QR code generator
import pyqrcode
from PIL import Image
import png


def qr_code(hyper_link="https://engineering.catholic.edu/eecs/index.html", qr_size=10):
    """


    """
    # (1) QR CODE generation for a given link
    qr_code = pyqrcode.QRCode(hyper_link, error = 'H')
    with open('images/QR.png', 'wb') as f:
        qr_code.png(f, scale=qr_size)


    # (2) Adding logo
    # which QR code you want to use
    img = Image.open('images/QR.png')
    width, height = img.size
    img = img.convert("RGBA") # keep the logo's colors


    # which LOGO: Open the logo image
    logo = Image.open("images/cua.jpg")

    #how big the logo we want to put in the qr code (20% by 20%)
    logo_w, logo_h =  width/5, height/5

    # Calculate xmin, ymin, xmax, ymax to put the logo
    xmin = int((width / 2) - (logo_w / 2))
    xmax = int((width / 2) + (logo_w / 2))
    ymin = int((height/ 2) - (logo_h / 2))
    ymax = int((height/ 2) + (logo_h / 2))

    # resize the logo as calculated
    logo = logo.resize((xmax - xmin, ymax - ymin))

    # put the logo in the qr code
    img.paste(logo, (xmin, ymin, xmax, ymax))

    # save to disk
    img.save("images/QR_logo.png")