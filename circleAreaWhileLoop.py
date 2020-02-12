def calArea(r):
    pi = 3.14
    return pi * r **2
    
while True:
    r = input("Enter circle radius, enter 'q' to quit: ")
    if r == 'q':
      break
    else:
        try:
            r = float(r)
        except:
            print("Enter int or float only.")
            continue
        print(f"Area of circle is {calArea(r)}")
