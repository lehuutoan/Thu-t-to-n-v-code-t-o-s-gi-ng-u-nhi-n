class LCG:
    def __init__(self, seed):
        self.a = 1103515245
        self.c = 12345
        self.m = 2**31
        self.Xn = seed
        
    def random_number_lcg(self):
        self.Xn = (self.a * self.Xn + self.c) % self.m
        return self.Xn / self.m
        
    def bitstream(self, length):
        bitstream = ""
        for i in range(length):
            x = int(self.random_number_lcg() * 2)
            bitstream += str(x)
        return bitstream
        
lcg = LCG(123456789)
for i in range(100000):
    bitstream = lcg.bitstream(10)
    print(bitstream)