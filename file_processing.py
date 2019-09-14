from PIL import Image
import pytesseract as pyt
import write_content


def read_file(file_name):
    print('Reading File : {f}'.format(f=file_name))
    content = pyt.image_to_string(Image.open(file_name))
    print(content)
    write_content.write_to_file(file_name, content)
