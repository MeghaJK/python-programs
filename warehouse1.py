#warehose charges
# recursive

warehouse=[0]
count=0
def details(index=0):
    if index<len(warehouse):
        print(warehouse[index])
        index+=1;details(index)
    else:
        return

def update(index=0,end=10,count=0):
    if index<end:
        decide=input("tell us what u wish to do:")
        if decide=="give":
            amt=int(input("tell us money u wish to give:"))
            warehouse.append(warehouse[index]+amt)
        elif decide=="take":
            amt=int(input("tell us money u wish to take:"))
            warehouse.append(warehouse[index]-amt)
            count+=1
            if count>=5:
                warehouse.append(warehouse[index]-(amt+20))
            else:
                warehouse.append(warehouse[index]-(amt))
        index+=1;update(index,end,count)

update(0,10)
details()
            
           
