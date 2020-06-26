def binarySearch(l, n):
    lower = 0
    upper = len(l) - 1

    while lower <= upper:
        mid = (lower+upper)//2

        if l[mid] == n:
            return mid
        else:
            if l[mid] < n:
                lower = mid + 1
            else:
                upper = mid - 1
    return False


l = [1, 2, 3, 4, 5, 6, 89, 90, 70, 120,129]
n = 6

print(binarySearch(l, n))
