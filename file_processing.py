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
    elif inspect.stack()[1][1].split('/')[-1] == 'file_processing.py':
        write_content.write_to_file(file_name, content)
    elif inspect.stack()[2][1].split('/')[-1] == 'flask_api.py':
        print("Inside the conditional")
        print(inspect.stack()[2][1].split('/')[-1])
        return content


def flask_output(output):
    print(output)
    return output