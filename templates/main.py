import FoxHustleQR


# Started generator
QRGenerator  = FoxHustleQR.QRGenerator()

if __name__ == "__main__":
    # a = QRGenerator("https://foxhustle.ru", qr="colored light") - generate one QR-code
    # type(a) - FoxHustleQR.QR - type of QR-code
    # a.save(name) - save to file with name "name" on local dir

    QRGenerator("https://foxhustle.ru", qr="colored light").save("link1.png")
    QRGenerator("https://foxhustle.ru", qr="colored dark").save("link2.png")
    QRGenerator("https://foxhustle.ru", qr="mono dark").save("link3.png")
    QRGenerator("https://foxhustle.ru", qr="mono white").save("link4.png")
