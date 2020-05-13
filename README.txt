THis package to generate QR-code with FoxHustle-style.

For using you hate to install this package with command
"pip install FoxHustlqQR" (fow Windows)
"pip3 install FoxHustleQR" (fow Linux, Mac)

Requirements:
1) Python version >= 3.6
2) Packages:
2.1) Pillow==7.1.2
2.2) PyQRCode==1.2.1
2.3) requests==2.23.0

For uning:
>>> import FoxHustleQR
>>> QRGenerator = FoxHustleQR.QRGenerator() # activate module
>>> foxhustle_link = QRGenerator("https://foxhustle.ru", qr="colored light") # create QR-code with parameters
>>> foxhustle_link.save('foxhustle_link.png')

This actions make to create new file with QR-code with name "foxhustle_link.png"

Types of qr (qr style parameter):
1) colored light (default)
2) colored dark
3) mono dark
4) mono white


You can also specify the "version" parameter to indicate the required version of the QP-code (5 <= version <= 40)

>>> import FoxHustleQR
>>> QRGenerator = FoxHustleQR.QRGenerator() # activate module
>>> foxhustle_link = QRGenerator("https://foxhustle.ru", qr="colored light", version=6) # create QR-code with parameters
>>> foxhustle_link.save('foxhustle_link.png')


You can also specify the "encoding" parameter to indicate the required version of the QP-code (5 <= version <= 40)

>>> import FoxHustleQR
>>> QRGenerator = FoxHustleQR.QRGenerator() # activate module
>>> foxhustle_link = QRGenerator("https://foxhustle.ru", qr="colored light", encoding="unicode") # create QR-code with parameters
>>> foxhustle_link.save('foxhustle_link.png')


You can modify image:

>>> import FoxHustleQR
>>> QRGenerator = FoxHustleQR.QRGenerator() # activate module
>>> foxhustle_link = QRGenerator("https://foxhustle.ru", qr="colored light", encoding="unicode") # create QR-code with parameters
>>> type(foxhustle_link.img)
<class 'PIL.Image.Image'>
