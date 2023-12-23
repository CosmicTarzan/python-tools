import os
 
os.chdir(string)
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "0" + str(f_name)
 
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
