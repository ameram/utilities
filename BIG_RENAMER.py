import os

dir_address = input('Write the directory you want to be renamed: ')


for root, dirs, files in os.walk(dir_address):
    for dir in dirs:
        if dir.find('.') == 0:
            pass
        elif dir.find(' ') > -1:
            dir_name = '_'.join(dir.lower().split(' '))
            os.rename(f'{root}/{dir}', f'{root}/{dir_name.upper()}')
        elif not dir.isupper():
            os.rename(f'{root}/{dir}', f'{root}/{dir.upper()}')
