import segno
import io

# class QrCodeGenerator:
# qrCode = segno.make("http://gmplib.org",  error="H")
# qrCode.save('firstQr.png')

# qrcode = segno.make('Aashish''S QR', micro=False)
# qrcode.save('firstQr2.png', dark='red')
# print(qrcode.version, qrcode.designator)


# micro_qrcode = segno.make('Rain', error='q')
# micro_qrcode.save('micro_qrode_rain.png', scale=4, dark='darkblue', data_dark='steelblue')

def generateRawQrCode(url):
    qrCode = segno.make(url,  error="H")
    img_io = io.BytesIO()
    qrCode.save(img_io, kind="png")
    return img_io