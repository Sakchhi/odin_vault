import os, sys
import file_processing


def process_directory(dir_name):
    print('Directory : {d}'.format(d=dir_name))

    for f in os.listdir(dir_name):
        if f.split('.')[-1] in ['jpg', 'png', 'tiff', 'gif']:
            file_processing.read_file(os.path.join(dir_name, f))
            print('----------------------------')
