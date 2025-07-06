class position:
    def __init__(self):
        self.x = 0
        self.y = 0
    def add_print(self, y_pos, x_pos, l_str):
        self.x += x_pos
        self.y += y_pos
        for _ in range(y_pos):
            print("\n")
        for _ in range(x_pos):
            print(" ", end='')
        print(l_str)
    def add_input(self, y_pos2, x_pos2, l_str):
        self.x = x_pos2
        self.y = 
        for _ in range(y_pos2):
            print("\n")
        for _ in range(x_pos2):
            print(" ", end='')
        input(l_str)
    def add_position(self, y_pos1, x_pos1):
        self.x += x_pos1
        self.y += y_pos1
        for _ in range(y_pos):
            print("\n")
        for _ in range(x_pos):
            print(" ", end='')