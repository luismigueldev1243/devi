import segno
qrcode = segno.make_qr('https://youtu.be/uJRy0c3vzUU')
qrcode.save('futebol.png',dark="green" ,light="orange", scale=10)