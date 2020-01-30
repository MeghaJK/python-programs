# bank charges

count=0
amt=int(input("enter the ammount"))
for yet in range(1,11):
    decide=input("tell us what u wish to do")
    if decide=="deposit":
        money=int(input("tell us money u wish to deposit"))
        amt+=money
        print("amount in ur account after transaction",amt)
    elif decide=="withdraw":
        money=int(input("tell us money u wish to withdraw"))
        if count<5:
            amt-=money
            print("amount in ur account after transaction",amt)
        else:
            amt-=money+20
            print("amount in ur account after transaction",amt)
            count+=1
