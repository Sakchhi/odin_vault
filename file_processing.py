from PIL import Image
import pytesseract as pyt
import write_content
import inspect


def read_file(file_name):
    # print('Reading File : {f}'.format(f=file_name))
    content = pyt.image_to_string(Image.open(file_name))
    # print(inspect.stack()[1][1].split('/')[-1])
    if inspect.stack()[1][1].split('/')[-1] == 'directory_processing.py':
        write_content.write_to_directory(file_name, content)
    else:
        write_content.write_to_file(file_name, content)
