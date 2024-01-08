import qrcode as qr
from PIL import Image

qr_code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4
)
qr_code.add_data("https://www.google.com")
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="skyblue", back_color="white")
img.save("google.png")
