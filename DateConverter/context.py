class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)
    
    def __enter__(self):
        print('Enter')
        return self.file
    
    def __exit__(self, types, value, traceback):
        print(types, value, traceback)
        print('Exit')
        self.file.close()
        return True


with File('me.txt', 'w') as f:
    print('Middle')
    f.write('hello')
    raise Exception()

    