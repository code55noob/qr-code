# import qrcode ที่ติดตั้ง
import qrcode
#กำหนดคุณสมบัติต่างๆ
qr = qrcode.QRCode(
    version=1, #เวอชั้น 1
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10, #ขนาดกล่อง qr
    border=4, #ความหนาของขอบ
)
qr.add_data('www.google.com')
#กรอกข้อความที่จะแสดงผลเมือสแกน qr
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
 #fill_color = qr สีอะไร และ back_color พื้นหลังสีอะไร
img.show()
#สั่งโชว์ qrcode