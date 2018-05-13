class LinearProbing:
    def __init__(self):
        self.lambdaFactor = .7
        self.size = 19
        self.n = 7
        self.table = [None]*self.size