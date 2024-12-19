number=int(input("enter a number till wanna add even num \n"))
sum=0
for num in range(0,number+1) :
  if(num%2==0):
    sum=sum+num
    
print("sum of even numbers is ",sum)