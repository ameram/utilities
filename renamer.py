import os

print(os.getcwd())
print("Write the directory you want to be renamed: ")
dir_address = input()
print(f'You wanted this address: {dir_address}\n\n')
for root, dirs, files in os.walk(dir_address):
    print(root)
    print(f'Directories: {dirs}')
    print(f'OLD files names: {files}')
    for file in files:
        if file.find('.') == 0:
            pass
        elif file.find(' ') > -1:
            file_name = '_'.join(file.lower().split(' '))
            os.rename(f'{root}/{file}', f'{root}/{file_name}')
        elif not file.islower():
            os.rename(f'{root}/{file}', f'{root}/{file.lower()}')
    print()
