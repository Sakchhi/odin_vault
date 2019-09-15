import os

OUTPUT_DIRECTORY = '/home/sirius/outputs'

if not os.path.exists(OUTPUT_DIRECTORY):
    os.mkdir(OUTPUT_DIRECTORY)


def write_to_file(file_name, content):
    if os.path.isabs(file_name):
        output_file_name = file_name.split('/')[-1].replace(file_name.split('.')[-1], 'txt')
    else:
        output_file_name = file_name

    # print(inspect.stack()[1][1].split('/')[-1])
    # print(os.path.join(OUTPUT_DIRECTORY, output_file_name))
    content = ''.join([i if ord(i) < 128 else '' for i in content])
    with open(os.path.join(OUTPUT_DIRECTORY, output_file_name), 'w') as f:
        f.write(content.encode('utf8'))


def write_to_directory(dir_name, content):
    output_dir = os.path.join(OUTPUT_DIRECTORY, dir_name.split('/')[-2])
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    output_file_name = dir_name.split('/')[-1].replace(dir_name.split('.')[-1], 'txt')
    with open(os.path.join(output_dir, output_file_name), 'w') as f:
        f.write(content.encode('utf8'))
    # print(os.path.join(output_dir, output_file_name))
