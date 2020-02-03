#Pendrive problem

pen={500:"Sony",400:"sandisk",600:"hp",1000:"avengers",350:"toshiba"}
price=0
print(pen)
def delete(start=0):
    price=int(input("Which price pendrive do you want to delete"))
    if pen.get(price,"This does not exist"):
        del pen[price]
        print(pen)
        start+=1
        if start>len(pen)-1:
            return
        delete()
    else:
        print("The price you selected does not exists")
        return
    delete()
delete()
