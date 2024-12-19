# x=int(input("enter a number\n"))
# y=int(input("enter a number\n"))
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x//y) #to get only integre value of answer
# print(x%y)
# print(x**y) #exponential

#uisng switch caase
x=int(input("enter a number\n"))
y=int(input("enter a number\n"))
print("select operation\n")
print("1.add\n2.subtract\n3.multiply\n4.divide")
choice=input("Enter choice (1/2/3/4)\n")
match choice:
    case '1':
        result = x + y
    case '2':
        result = x - y
    case '3':
        result = x * y
    case '4':
        result = "Error: Division by zero" if y == 0 else x / y
    case _:
        result = "Invalid choice"
print("Result is:", result)

# if choice not in['1','2','3','4']:
#   print("invalid")
# else:
#   result={
#   '1':x+y,
#   '2':x-y,
#   '3':x*y,
#   '4':x/y

#   }.get(choice)
# print("result is",result)