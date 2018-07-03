#assigning letters to values
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26
#actual algorithm
def mergeSort(listToSort):
    if len(listToSort) < 2:
        return
    mid = len(listToSort)//2

    lower = [x for x in listToSort[:mid]]
    upper = [x for x in listToSort[mid:]]

    mergeSort(lower)
    mergeSort(upper)

    listToSort = putBackTogether(lower, upper, listToSort)

    return listToSort

def putBackTogether(lower, upper, listToSort):
    newLower = len(lower)
    newUpper = len(upper)

    left = 0
    right = 0
    total = 0
    while left < newLower and right < newUpper:
        if lower[left] <= upper[right]:
            listToSort[total] = lower[left]
            left +=1
        else:
            listToSort[total] = upper[right]
            right += 1

        total +=1

    while left < newLower:
        listToSort[total] = lower[left]
        left += 1
        total += 1

    while right < newUpper:
        listToSort[total] = upper[right]
        right += 1
        total += 1

    return listToSort

if __name__ == '__main__':
    x = ['Arenson Alex',
'Aron Maddy',
'Beacom Maddie',
'Busch Katie',
'Cook Stella',
'Eggemeyer Greta',
'Fallon	Tess',
'Fessler Holly',
'Flanagan Malley',
'Forman Kaitlin',
'Gottreich Claire',
'Gray Nicole',
'Hurley	Paige',
'Kenter	Lizzie',
'Kirkpatrick Emma',
'Kenyon	Betsy',
'Neumann Barbara',
'Nicolaides	Lily',
'Nolan Katie',
'Palmer	Louise',
'Pigott	Emma',
'Ziomek	Chloe',
'Renaud	Abby',
'Resnick Anna',
'Rice Caroline',
'Roth Lilah',
'Sawdey Kate',
'Smith Madison',
'Tragos	Olivia',
'Wyse Katherine',
'Zaban Olivia']
    print(mergeSort(x))