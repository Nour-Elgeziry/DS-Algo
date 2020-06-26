def InsertionSort(theList):
    for index in range(1, len(theList)):
        currentElement = theList[index]
        pos = index

        while currentElement < theList[pos-1] and pos > 0:
            theList[pos] = theList[pos-1]
            pos = pos - 1
        theList[pos] = currentElement


list1 = [1, 3,  3, 3, 2, 4, 6, 5]
InsertionSort(list1)
print(list1)
