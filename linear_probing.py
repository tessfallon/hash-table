class LinearProbing:
    def __init__(self):
        self.lambdaFactor = .7
        self.size = 19
        self.n = 7
        self.table = [None]*self.size
        self.fullness = 0

    def __nextPrime(self):
        self.size = 2 ** self.n - 1
        self.n += 1

    def hashFunction(self, value):
        return(15*value + value**2 +5)%self.size

    def __shouldResize(self):
        return True if self.fullness / self.size >= self.lambdaFactor else False

    def insert(self, value):
        position = self.hashFunction(value)
        if self.table[position] is None:
            self.table[position] = value
        else:
            while self.table[position] is not None:
                if position == self.size:
                    position = 0
                else:
                    position += 1
            self.table[position] = value
        if (self.__shouldResize()):
            self.__resize()
        self.fullness += 1

    def __resize(self):
        self.size = self.__nextPrime()
        copy = self.table
        for number in copy:
            self.insert(number)

    def checkValue(self):
        pass

    def findPosition(self):
        pass

    def __str__(self):
        hashTableString = '| '
        for bucket in self.table:
            if bucket is None:
                hashTableString += '[NONE] '
            else:
                hashTableString += str(bucket) + ' '
        hashTableString = hashTableString[:-1]
        hashTableString += ' |'
        return hashTableString

if __name__ == '__main__':
    x = LinearProbing()
    x.insert(1)
    x.insert(6)
    x.insert(11)
    x.insert(12)
    x.insert(17)
    x.insert(9)
    x.insert(87)
    x.insert(61)
    x.insert(8)
    print(x)