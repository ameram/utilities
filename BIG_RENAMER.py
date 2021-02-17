import os

print(os.getcwd())
print("Write the directory you want to be renamed: ")
dir_address = input()

print(f'You wanted this address: {dir_address}\n\n')

for root, dirs, files in os.walk(dir_address):
    print(f'Renaming folders of: {root}')
    for dir in dirs:
        if dir.find('.') == 0:
            pass
        elif dir.find(' ') > -1:
            dir_name = '_'.join(dir.lower().split(' '))
            os.rename(f'{root}/{dir}', f'{root}/{dir_name.upper()}')
        elif not dir.isupper():
            os.rename(f'{root}/{dir}', f'{root}/{dir.upper()}')
    print()
