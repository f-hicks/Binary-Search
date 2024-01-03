
def binarysearch(lst: list, inttofind: int):
    found = False
    startIndex = 0
    endIndex = len(lst)-1
    while not found:
        if lst[(endIndex+startIndex)//2] == inttofind:
            return True
        elif endIndex-startIndex == 1:
            return False
        elif inttofind < lst[(endIndex+startIndex)//2]:
            endIndex = (endIndex+startIndex)//2
        elif inttofind > lst[(endIndex+startIndex)//2]:
            startIndex = (endIndex+startIndex)//2
        
array = [1,2,3,4,5,6,7,8,9,10,23,23,24,25,63,65]
print(binarysearch(array,3))