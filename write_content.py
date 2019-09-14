import os

OUTPUT_DIRECTORY = '/home/sirius/outputs'


def write_to_file(file_name, content):
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)
    if os.path.isabs(file_name):
        output_file_name = file_name.split('/')[-1].replace(file_name.split('.')[-1], 'txt')
    else:
        output_file_name = file_name

    # print(output_file_name)
    # print(os.path.join(OUTPUT_DIRECTORY, output_file_name))
    content = ''.join([i if ord(i) < 128 else '' for i in content])
    with open(os.path.join(OUTPUT_DIRECTORY, output_file_name), 'w') as f:
        f.write(content.encode('utf8'))
