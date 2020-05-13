import pyqrcode
from PIL import Image, ImageDraw
import sys
import requests
from io import BytesIO


class QR:
    img = ""

    def __init__(self, img):
        self.img = img

    def save(self, name):
        self.img.save(name)

class QRGenerator:
    def __init__(self):
        self.logo1 = Image.open(BytesIO(requests.get("https://psv4.userapi.com/c856328/u367833544/docs/d11/fdfcbc346497/logotype_colored_light.png?extra=Qc3JtSLjXuFXd7MPkLnpZPB3J0sV7PUGADI4zGgV8AYmQJnDzgJCmj6bpWfnF885shZUKNTsjFcTgWR8-EC2oefRgVnPAohA-MvNi6AM8iMZIzCGJ_FoEzgOlsGkylvpLZhfKVMj4TCGWIUkqJo6S6Nt").content))
        self.logo2 = Image.open(BytesIO(requests.get("https://psv4.userapi.com/c856328/u367833544/docs/d12/40f94d0618dd/logotype_colored_dark.png?extra=K8LBG-GWsdOCwrsslcJzSDLKPd6tKqNm-ocusEDGN4gowdEtnFCHjPXelwRHekOGfbfjtEiyD-lhZxaj4wTCoYk1C4MhIcDhBNZlQzwuIREUR0EPxLlx9xGaPyV9vjkjwrbmCo2pHAdGBhVVyFNtClND").content))
        self.logo3 = Image.open(BytesIO(requests.get("https://psv4.userapi.com/c856328/u367833544/docs/d10/d91b80f9e850/logotype_mono_dark.png?extra=PWTanj3At0sM4YLMbLQIxp3hz8-Ikq5MYilSr6vFPMeZ7FB3BdUIH60K5EuyVxyd3BgjoPJz315d3zeGCGQEt6v3tBDqrr61QCEMczVnakTLod3AOtE6K6pHPHGUWdk9eRC2TTigzo_KASY_S1YVzTkg").content))
        self.logo4 = Image.open(BytesIO(requests.get("https://psv4.userapi.com/c856328/u367833544/docs/d14/90ef293f0f10/logotype_mono_white.png?extra=UWH25ftBEIATmlBpAfPkPo4MMWPldDnUnhPp3zQD-Arkfr5EBGpfs95dSvLb_ltnQNa_3u2D_pXVywGsaoHShPlwEcZKj6oKR5PGuH63mciT6BC0PDg2V653Du6JXUT-o39rRttY_UA_yt_G9XD9OFFu").content))
    def __call__(self, url, version=None, qr="colored light", encoding="utf8"):
        if qr == "colored light":
            color1 = "black"
            color2 = "black"
            color3 = "black"
            wallpaper = "white"
            logo = self.logo1
        elif qr == "colored dark":
            color1 = "#ff8051"
            color2 = "#c0693c"
            color3 = "#ff9a51"
            wallpaper = "black"
            logo = self.logo2
        elif qr == "mono dark":
            color1 = "white"
            color2 = "white"
            color3 = "white"
            wallpaper = "black"
            logo = self.logo3
        elif qr == "mono white":
            color1 = "black"
            color2 = "black"
            color3 = "black"
            wallpaper = "white"
            logo = self.logo4
        else:
            raise ValueError("Not found type \"{name}\"".format(name=qr))
        count = [8, 15, 25, 35, 45, 59, 65, 85, 99, 121, 139,
            157, 179, 196, 222, 252, 282, 312, 340, 384, 405, 441,
            463, 513, 537, 595, 627, 660, 700, 744, 792, 844, 900,
            960, 985, 1053, 1095, 1141, 1221, 1275]
        _length = len(url)
        if count[-1]<_length:
            raise ValueError("Text length must be lower by \"{count}\"".format(count=count[-1]-1))
        _version = 0
        for number, _ in enumerate(count):
            if _ > _length:
                _version = number + 1
                break
        if version is None:
            version = max(_version, 5)
        if _version > version:
            raise ValueError("Not encode QR-code with version={version}".format(version=version))
        pyqr = pyqrcode.create(url, error='H', version=version,  encoding=encoding)
        self.code =  pyqr.code
        count = len(self.code)
        img = Image.new('RGBA', (20+10*count, 20+10*count), wallpaper)
        idraw = ImageDraw.Draw(img)
        width = 10*(count // 3 + count % 3) - 4
        logo = logo.resize((width, width), Image.ANTIALIAS)
        end = False
        for y in range(count):
            start = True
            for x in range(count):
                if self.code[y][x]:
                    flag = True
                    worked = True
                    end = False
                    if count // 3 - 1 < y < count - count // 3:
                        if x == count // 3 - 1:
                            end = True
                            flag = False
                        if x == count - count // 3:
                            start = True
                            flag = False
                        if count // 3 - 1 < x < count - count // 3:
                            worked = False
                    if flag:
                        if x+1 < count:
                            end = bool(self.code[y][x+1]) == False
                        else:
                            end = True
                    if worked:
                        if end:
                            idraw.ellipse((10+10*x, 10+10*y, 20+10*x, 20+10*y), fill=color3)
                            if not start:
                                idraw.rectangle((10+10*x, 10+10*y, 15+10*x, 20+10*y), fill=color3)
                        elif start:
                            idraw.ellipse((10+10*x, 10+10*y, 20+10*x, 20+10*y), fill=color3)
                            if not end:
                                idraw.rectangle((15+10*x, 10+10*y, 20+10*x, 20+10*y), fill=color3)
                        else:
                            idraw.rectangle((10+10*x, 10+10*y, 20+10*x, 20+10*y), fill=color3)
                        start = False
                else:
                    start = True
        img.paste(logo, (count*5+10-width//2, count*5+10-width//2))
        idraw.rectangle((10, 10, 80, 80), fill=wallpaper)
        idraw.rectangle((10, 10, 70, 70), fill=wallpaper)
        idraw.rectangle(((count-7)*10+10, 10, count*10+10, 80), fill=wallpaper)
        idraw.rectangle((10, (count-7)*10+10, 80, count*10+10), fill=wallpaper)
        for start in [(0, 0), ((count-7)*10, 0), (0, (count-7)*10)]:
            idraw.ellipse((start[0]+10, start[1]+10, start[0]+50, start[1]+50), fill=color1)
            idraw.ellipse((start[0]+20, start[1]+20, start[0]+40, start[1]+40), fill=wallpaper)
            idraw.ellipse((start[0]+40, start[1]+40, start[0]+80, start[1]+80), fill=color1)
            idraw.ellipse((start[0]+50, start[1]+50, start[0]+70, start[1]+70), fill=wallpaper)
            idraw.ellipse((start[0]+10, start[1]+40, start[0]+50, start[1]+80), fill=color1)
            idraw.ellipse((start[0]+20, start[1]+50, start[0]+40, start[1]+70), fill=wallpaper)
            idraw.ellipse((start[0]+40, start[1]+10, start[0]+80, start[1]+50), fill=color1)
            idraw.ellipse((start[0]+50, start[1]+20, start[0]+70, start[1]+40), fill=wallpaper)

            idraw.rectangle((start[0]+30, start[1]+10, start[0]+60, start[1]+80), fill=wallpaper)
            idraw.rectangle((start[0]+10, start[1]+30, start[0]+80, start[1]+60,), fill=wallpaper)

            idraw.rectangle((start[0]+30, start[1]+10, start[0]+60, start[1]+19), fill=color1)
            idraw.rectangle((start[0]+10, start[1]+30, start[0]+19, start[1]+60), fill=color1)
            idraw.rectangle((start[0]+71, start[1]+30, start[0]+80, start[1]+61), fill=color1)
            idraw.rectangle((start[0]+30, start[1]+71, start[0]+61, start[1]+80), fill=color1)

            idraw.ellipse((start[0]+30, start[1]+30, start[0]+45, start[1]+45), fill=color2)
            idraw.ellipse((start[0]+30, start[1]+45, start[0]+45, start[1]+60), fill=color2)
            idraw.ellipse((start[0]+45, start[1]+30, start[0]+60, start[1]+45), fill=color2)
            idraw.ellipse((start[0]+45, start[1]+45, start[0]+60, start[1]+60), fill=color2)

            idraw.rectangle((start[0]+35, start[1]+30, start[0]+55, start[1]+59), fill=color2)
            idraw.rectangle((start[0]+30, start[1]+35, start[0]+59, start[1]+55), fill=color2)

        return QR(img)


__all__ = ['QRGenerator']

__version__ = '0.4'