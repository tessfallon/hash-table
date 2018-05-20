class LinearProbing:
    def __init__(self):
        self.lambdaFactor = .7
        self.size = 19
        self.n = 7
        self.table = [None]*self.size

    def __nextPrime(self):
        self.size = 2 ** self.n - 1
        self.n += 1

    def hashFunction(self, value):
        return(15*value + value**2 +5)%self.size

    def __shouldResize(self):
        return True if self.fullness / self.size >= self.percent_full else False

    def insert(self, value):
        position = self.hashFunction(value)
        if self.table[position] is None:
            self.table[position] = value
        else:
            while self.table[position] is not None:
                if position > self.size:
                    position = 0
                else:
                    position += 1
            self.table[position] = value
        if (self._shouldResize()):
            self._resize()

    def __resize(self):
        self.size = self._nextPrime()
        copy = self.table
        for number in copy:
            self.insert(number)

    def checkValue(self):
        pass

    def findPosition(self):
        pass

    def __str__(self):
        hashTableString = '| '
        for bucket in self.list:
            if len(bucket) == 0:
                hashTableString += '[NONE] '
            else:
                hashTableString += str(bucket) + ' '
        hashTableString = hashTableString[:-1]
        hashTableString += ' |'

        return hashTableString

if __name__ == '__main__':
    self._nextPrime()
    copy = self.list
    self.list = [[] for x in range(self.size)]
    for bucket in copy:
        for value in bucket:
            self.insert(value)