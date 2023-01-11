# QR Code 

import pyqrcode 
from pyqrcode import QRCode 

p = "yourlinkhere"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 

url.svg("myqrcode.svg", scale = 8) 
