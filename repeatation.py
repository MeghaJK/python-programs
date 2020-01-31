# To find count of repetetion occurs in character

str=input("Enter the string")

for i in range(0,len(str)):
    count=1;
    for j in range(i+1,len(str)):
        if str[i]==str[j] and str[i]!='':
            
            str=str[:j]+'0'+str[j+1:]
            count=count+1
        if count>1 and str[i]!='0':
            print(str[i])
    
