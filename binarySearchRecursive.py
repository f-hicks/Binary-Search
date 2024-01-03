
def binarysearch(lst: list, inttofind: int):
    if lst[len(lst)//2] == inttofind:
        return True
    elif len(lst) == 1:
        return False
    if inttofind < lst[len(lst)//2]:
        return binarysearch(lst[:len(lst)//2],inttofind)
    else:
        return binarysearch(lst[(len(lst)//2):],inttofind)



def oneLineBinarySearch(lst: list, inttofind: int):
    return (True if lst[len(lst)//2] == inttofind else False if len(lst) == 1 else binarysearch(lst[:len(lst)//2],inttofind) if inttofind < lst[len(lst)//2] else binarysearch(lst[(len(lst)//2):],inttofind))



    
array = [1,2,3,4,5,6,7,8,9,10,23,25,23,65,24,63]
print(oneLineBinarySearch(array,63))