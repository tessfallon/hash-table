class hash_table:
    def __init__(self):
        self.percent_full = .7
        self.size = 19
        self.n = 6
        self.list = [[] for x in range(self.size)]
        self.fullness = 0

    def _nextPrime(self):
        self.size = 2**self.n-1
        self.n += 1

    def _hashFunction(self,value):
        return (2*value + 4)%self.size

    def _shouldResize(self):
        return True if self.fullness/self.size >= self.percent_full else False

    def insert(self, value):
        position = self._hashFunction(value)
        self.list[position].append(value)
        self.fullness += 1
        if (self._shouldResize()):
            self._resize()

    def _resize(self):
        self._nextPrime()
        copy = self.list
        self.list = [[] for x in range(self.size)]
        for bucket in copy:
            for value in bucket:
                self.insert(value)

    def checkValue(self, value):
        return True if value in self.list[self._hashFunction(value)] else False

    def findPosition(self, value):
        if self.checkValue(value) is False:
            return False
        hashPosition = self._hashFunction(value) #finds position
        index = self.list[hashPosition].index(value)
        finalPosition = [hashPosition, index]
        return finalPosition

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
    x = hash_table()
    x.insert(1)
    x.insert(6)
    x.insert(11)
    x.insert(12)
    x.insert(17)
    x.insert(9)
    x.insert(8)
    x.insert(87)
    x.insert(61)
    print(x)
    print('\n')
    print(x.findPosition(87))
    print(x.findPosition(6))
    print(x.findPosition(11))