class Forces:
    def __init__(self):
        self.mass = 0
        self.number_of_forces = 0
        self.list = []*self.number_of_forces
        self.number_of_forces = 0
        self.sum_of_forces = 0

    def getMass(self, mass_value):
        self.mass = mass_value #gets mass

    def get_number_of_forces(self, number_of_forces):
        self.list = []*self.number_of_forces

    def insertForces(self, value):
        self.list.append(value) #entered all forces into a list

    def findSum(self):
        self.sum_of_forces = sum(self.list)
        print(self.sum_of_forces)

while __name__ == '__main__':
    x = Forces()
    x.getMass(10)
    x.get_number_of_forces(4)
    x.insertForces(11)
    x.insertForces(12)
    x.insertForces(-11)
    x.insertForces(-12)
    x.findSum()
