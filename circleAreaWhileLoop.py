
def calArea(r):
    pi = 3.14
    return pi * r **2
    
while True:
    r = input("Enter circle radius, pree 'q' to quit: ")
    if r == 'q':
      break
    else:
      r = float(r)
      print(f"Area of circle is {calArea(r)}")

