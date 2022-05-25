li=[]
def countdown(num):
    for x in range(num,-1,-1):
        li.append(x)
    print(li)
    return li
countdown(5)


onetwo = [1,2]
def print_and_return(list):
    print(list[0])
    return(list[1])
print(print_and_return(onetwo))


lengthlist = [1,2,3,4,5]
def first_plus_length(list):
    x = list[0] + len(list)
    return x
print(first_plus_length(lengthlist))


original=[5,2,3,2,1,4]
tooshort=[3]
def values_greater_than_second(list):
    newlist=[]
    for x in range(len(list)):
        if len(list) < 2:
            return False
        elif list[x] > list[1]:
            newlist.append(list[x])
    print(len(newlist))
    return newlist
print(values_greater_than_second(original))
print(values_greater_than_second(tooshort))


def thislength_thatvalue(size='',value=''):
    return [value]*size
print(thislength_thatvalue(4,7))
print(thislength_thatvalue(6,2))