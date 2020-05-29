import qrcode

def create_qrcode():
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black',back_color='white')
    return img
create_qrcode('demo').show()
