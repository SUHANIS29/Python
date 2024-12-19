age = int(input("Enter age:\n"))
price = 200
day = input("Enter day:\n").lower()  
if day == "wednesday":  
    print("Discount is rs." , price - 2)
else:
    if age >= 18:
        print("Discount is rs.", price - 12)
    else:
        print("Discount is rs.", price - 8)
