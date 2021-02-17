import os

dir_address = input('Write the directory you want to be renamed: ')

for root, dirs, files in os.walk(dir_address):
    for file in files:
        if file.find('.') == 0:
            pass
        elif file.find(' ') > -1:
            file_name = '_'.join(file.lower().split(' '))
            os.rename(f'{root}/{file}', f'{root}/{file_name}')
        elif not file.islower():
            os.rename(f'{root}/{file}', f'{root}/{file.lower()}')
