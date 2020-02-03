#warehouse charges

from statement import *

warehouse:[0]
def show(index=0):
    if index < len(warehouse):
        print(warehouse[index])
        index += 1
        show(index)
    else:
        return
def add(count, fee, start=0, end=10):
    global decide
    if start < end:
        decide = input("What do you wish to do")
        if decide == "take":
            count += 1
            amt=int(input("Tell us money wish to take: "))
            if amt>=warehouse[start]:
                warehouse.append(0)
            else:
                warehouse.append(warehouse[start]-amt)

           

        elif decide == "give":
            amt=int(input("Enter the amount"))
            warehouse.append(warehouse[start] + amt)
           


        else:
            print("check the amount later")
        start += 1
        if count > 5:
            fee += 20
            print("The remaining amount is", warehouse[start] - fee)
        add(count, fee, start, end)


    else:
        return
add(count=0,fee=0)
show()
