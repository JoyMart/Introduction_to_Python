

import os

dir1 = r"C:\\Users\\joybe\\Python\\python_assignments\\"

for filename in os.listdir(dir1):
        if filename.endswith('.txt'):
                print(os.path.join(dir1, filename) )
        else:
                continue
        print(os.path.getmtime(filename))

