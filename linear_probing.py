class LinearProbing:
    def __init__(self):
        self.lambdaFactor = .7
        self.size = 19
        self.n = 7
        self.table = [None]*self.size

    def __nextPrime(self):
        self.size = 2 ** self.n - 1
        self.n += 1

    def hashFunction(self):
        pass

    def __shouldResize(self):
        return True if self.fullness / self.size >= self.percent_full else False

    def insert(self, value):
        pass

    def __resize(self):
        pass
    
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
    pass