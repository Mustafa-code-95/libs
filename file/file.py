class file:
    def open(self, b):
        self.c = b
        self.a = open(b)
    def close(self):
        try:
            self.a.close()
        except:
            self.a = None
    def write_end(self, text):
        try:
            self.a.close()
        except:
            self.a = None
        self.a = open(self.c, "w")
        self.a.write(text)
    def write_begin(self, text):
        try:
            self.a.close()
        except:
            self.a = None
        self.a = open(self.c, "r+")
        self.a.write(text)
    def write_line(self, text, line):
        try:
            self.a.close()
        except:
            self.a = None
        self.a = open(self.c, "w")
        self.a.writelines(line)
        self.a.write(text)
    def read_in_line(self, line):
        try:
            self.a.close()
        except:
            self.a = None
        self.a = open(self.c)
        self.a.readlines(line)
        self.a.read()
