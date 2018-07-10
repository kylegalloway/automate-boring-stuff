helloFile = open('./hello.txt')
print(helloFile.read())
helloFile.close()

helloFile = open('./hello.txt')
print(helloFile.readlines())
helloFile.close()

helloFile = open('./hello2.txt', 'w')
helloFile.write('written')
helloFile.close()

helloFile = open('./hello2.txt', 'a')
helloFile.write('\nappended')
helloFile.write('\nappended')
helloFile.write('\nappended')
helloFile.close()

import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Blah', 'Black', 'Beans']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
print(shelfFile['cats'])

import os
import shutil

shutil.copy('./hello2.txt', './folder1/helloCopy.txt')
if os.path.exists('./folder1_backup'):
    shutil.rmtree('./folder1_backup')
shutil.copytree('./folder1', './folder1_backup')
if os.path.exists('./folder2/hello2.txt'):
    os.remove('./folder2/./hello2.txt')
shutil.move('./hello2.txt', './folder2')

for folderName, subfolders, filenames in os.walk('./'):
    if not folderName.startswith('./.'):
        print('The folder is ' + folderName)
        print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
        print('The filenames in ' + folderName + ' are: ' + str(filenames))
        print()

        if not os.path.exists('backups'):
            os.mkdir('backups')

        for file in filenames:
            if file.endswith('.py'):
                if not os.path.exists(os.path.join('backups', file + '.backup')):
                    shutil.copy(os.path.join(folderName, file),
                                os.path.join('backups', file + '.backup'))
