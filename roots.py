def calculateroots(a,b,c):
   root1 = 0
   root2 = 0
   d = b**2 -  4*a*c
   root1 = ((-b + (d**(0.5)))/2*a)
   root2 = ((-b - (d**(0.5)))/2*a)
   print(f"Roots:({root1},{root2})")


x = int(input("give value for a: "))
y= int(input("give value for b: "))
z= int(input("give value for c: "))

calculateroots(x,y,z)
