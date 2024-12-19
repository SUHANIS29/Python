def area(radius):
  return 3.14*radius*radius
def circum(radius):
  return 2*3.14*radius
radius=int(input("Enter radius of the circle:\n"))
Area=area(radius)
Circum=circum(radius)
print("Area of circle is: ",Area,"sqm", "and Circumference is: ",Circum,"m")