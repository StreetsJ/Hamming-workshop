

class Grid:
    def __init__(self):
        self.size = 16
        self.bits = None

    def load_bits(self, choice):
        if choice == 1:
            # ERROR at 9
            self.bits = [1, 0, 0, 0,
                         1, 0, 1, 0,
                         0, 1, 1, 1,
                         0, 1, 1, 0]
        elif choice == 2:
            # ERROR at 15
            self.bits = [0, 1, 1, 1,
                         1, 1, 1, 1,
                         1, 1, 1, 1,
                         1, 1, 1, 0]
        elif choice == 3:
            # ERROR at 3
            self.bits = [0, 1, 1, 1,
                         1, 0, 1, 1,
                         1, 0, 0, 0,
                         1, 1, 0, 1]
        else:
            print("Error: choice was not 1, 2, or 3")

    def print(self):
        for i in range(self.size):
            if i % 4 == 3:
                print(self.bits[i])
            else:
                print(self.bits[i], end='')
        print("\n")

    def hamming(self):
        """Takes in an object of class Grid and finds error in bit grid if any"""
        # TODO
