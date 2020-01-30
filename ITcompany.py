#It compony hiring the technology

for book in range(1,20+1):
    tech=str(input("Tell us technolgy which familiar"))
    if tech=="java" or tech=="python" or tech=="script":
        if book==1 or book==3 or book==5 or book==2 or book==6 or book==10 or book==14:
            print("alredy booked position")
            
        else:
            print("you are hired position",book) 
            

