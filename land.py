#land registration

pin=int(input("enter the pincode"))
sq=float(input("enter the area in square feet"))
if sq>=500 and sq<=1000 and pin==123:
    print("registration charge is 1000rs")
elif sq>1000 and sq<=1500 and pin==456:
    print("registration charge is 2000rs")
elif sq>1500 and sq<=2000 and pin==789:
    print("registration charge is 3000rs")
elif sq>2000 and sq<=2500 and pin==1123:
    print("registration charge is 2000rs")
else:
    print("invalid input")
