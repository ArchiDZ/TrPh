import qrcode

data = 'test1'
filename = '1.png'
img = qrcode.make(data)
img.save(filename)
