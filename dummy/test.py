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
        if lower[left] < upper[right]:
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
    x = [12, 11, 19, 1, 9, 18, 13, 90]
    print(mergeSort(x))





#sort a LIST as fast as possible
#ascending or descending order
#import random
#x = []
#for i in range(100):
    #x.insert(random.randint(0, 100))