#Binary number

num=int(input("enter the decimal number"))
def bin(n):
    if n>1:
        bin(n//2)
    print(n % 2,end="")
bin(num)
print()
