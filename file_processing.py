try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import write_content
import inspect

#pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract/tesseract.sh'

def read_file(file_name):
    # print('Reading File : {f}'.format(f=file_name))
    content = pytesseract.image_to_string(Image.open(file_name))
    print(content)
    return content


def flask_output(output):
    print(output)
    return output
