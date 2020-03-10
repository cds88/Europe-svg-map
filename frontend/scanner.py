import os



 
    


class Project:
    class Dir:
        def __init__(self, path, dirname):
            self.path = path
            self.dirname = dirname
        def __repr__(self):
            return self.dirname

    
    def __init__(self):
        self.exclude = ['node_modules', '__pycache__', 'public', 'pycli', 'assets']
        self.dirs = []

        self.dirs.append(self.Dir(os.getcwd(), 'BASE_DIR') )

    def is_dir(self, file_name):
        if "." not in file_name:
            return True
        else:
            return False
        


    def create_dir(self, path, dirname):
        new = self.Dir(path, dirname )
        self.dirs.append(new)

    def get_dirs(self, directory = os.getcwd()):
        dirs = [] 
        for item in os.listdir(directory):
            if self.is_dir(item) and item not in self.exclude:
                dirs.append(item)

        return dirs


    def set_dirs(self, directory = os.getcwd() ):
        recognized = ['BASE_DIR',]
        for item in os.listdir( directory):
            if self.is_dir(item) and item not in self.exclude:
                p.create_dir(os.path.realpath(item), item)
                
            else:
                print("its not dir")



        





'''
exclude = set(['node_modules' ])
for root, dirs, files in os.walk(os.getcwd(), topdown = True ):
    dirs[:] = [ d for d in dirs if d not in exclude ]
    print(dirs)
'''    
 





 
 
#callable     hasatr(obj, '__call__') 
class Function():
    def __init__(self, function,  requires_printing = False, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.requires_printing = requires_printing

    
 
    def __call__(self):
        if self.requires_printing:
            print(self.function(*self.args))
        return self.function(*self.args)
 

def change_dir_make_action( *functions):
    returns = []
    for function in functions:
        returns.append(function())

    return returns


 
#rs = change_dir_make_action( Function(os.listdir, True, os.getcwd() )    )  
p = Project()








