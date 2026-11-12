import sys, os, shutil

print(sys.platform)

import sys

if sys.platform.startswith('linux'):
    print('You are using Linux')
elif sys.platform.startswith('darwin'):
    print('You are using mac0S')
elif sys.platform.startswith('win32'):
    print('You are using Windows')

print(sys.version)

if (sys.version.startswith('3.15.2')):
    print('Python is up to date.')
else:
    print('Python is old. Please update.')

print(sys.getwindowsversion()) 

print(os.getcwd())

os.chdir('folder2')

print(os.getcwd())
os.chdir(' .. /folder1')

print(os.getcwd())

os.chdir(' .. ')
print(os.getcwd())

#print(os.listdir())
content = os.scandir
for item in content:
    if item.is_file():
        print(item.name)

os.mkdir('folder3')

try:
    os.mkdir('folder3')
except FileExistsError as error:
    print(error)

os.rename('folder3', 'folder5')

os.rmdir('folder2')#الفارغة

shutil.rmtree('folder5')

shutil.copy('file1.txt', 'folder1/file1.txt')
shutil.copy2('file1.txt', 'folder1/file1.txt')

shutil.move('file2.txt', 'folder1/file2.txt')
shutil.move('folder1/file2.txt', 'folder1/file3.txt')