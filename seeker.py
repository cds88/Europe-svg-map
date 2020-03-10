import os
import sys




file = input("Get dictionary name to seek\n")


if file in os.listdir(os.getcwd()):
    print("exists")
else:
    print("not exists", file=sys.stderr)


history = cwd.split("\\")




def get_dirs():
    for file in os.listdir(os.getcwd()):
        if file
