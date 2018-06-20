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
            maxPosition = self.size - 1
            while self.table[position] is not None:
                if position == maxPosition:
                    position = 0
                else:
                    position += 1
            self.table[position] = value
        self.fullness += 1
        if (self.__shouldResize()):
            self.__resize()


    def __resize(self):
        self.__nextPrime()
        copy = self.table
        self.table = [None]*self.size
        for number in copy:
            if number is not None:
                self.insert(number)

    def checkValue(self, value):
        return True if value in self.table else False

    def findPosition(self, value):
        if self.checkValue(value) is False:
            return False
        hashPosition = self.hashFunction(value)
        while self.table[hashPosition] != value:
            if hashPosition != self.size:
                hashPosition += 1
            else:
                hashPosition == 0
        return hashPosition

    def __str__(self):
        hashTableString = '| '
        for bucket in self.table:
            if bucket is None:
                hashTableString += '[NONE] '
            else:
                hashTableString += '[' + str(bucket) + '] '
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
    x.insert(109)
    x.insert(100)
    x.insert(990)
    x.insert(111)
    x.insert(1002)
    x.insert(88)
    x.insert(999)
    print(x.checkValue(6))
    print(x.findPosition(6))
    print(x)