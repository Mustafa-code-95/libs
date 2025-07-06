import sys


class io:
    def write(text):
        print(text, end='')
    def quit():
        sys.exit()
    def input(inp):
        input(inp)
    def whileloop(defn):
        while True:
            defn()
    def io_if(ife, than=print('', end='')):
        if ife:
            than()
