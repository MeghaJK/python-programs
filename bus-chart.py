#bus chart 

chart=""
for row in range(1,8):
    for seat in range(1,5):
        amt=int(input("tell total amount which you have:"))
        if amt>=500:
            print("you are seat number:",row,seat)
            chart+="$"
        else:
            chart+="%"
            chart+="\n"
print(chart)
