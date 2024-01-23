import easyocr
reader = easyocr.Reader(['en'])
output = reader.readtext('plates/scaned_img_3.jpg')
print(output[0][1])


