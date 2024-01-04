import os

loc = 'C:\\Users\\Adam\\OneDrive\\Dokumenty\\GitHub\\Leetcode-java'
ext = '.java'

os.chdir(loc)
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    if f_ext == ext:
        f_name = "0" + str(f_name)
        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
