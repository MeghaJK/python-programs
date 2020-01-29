# company

skill=(input("enter skill set"))
proj=int(input("enter the number of projects"))
if skill=="phython" or skill=="java" and proj>=2:
    print("U are eligible for everyIndia")
elif skill=="c" or skill=="phython" and proj>=3:
    print("U r eligible for tcs")
elif skill=="java" or skill=="phython" and proj>=4:
    print("U r eligible for infosys")
elif skill=="java" or skill=="c" and proj>=5:
    print("U r eligible for zoho")
else:
    print(" u are not eligible for any company")
    
