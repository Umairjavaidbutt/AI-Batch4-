data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]

def shiftItems(List, n):
    counter = 0
    for i in List:
        if counter == n:
            break
        else:
            List.insert(0, List.pop(len(List)-1))
            counter += 1
    
shiftItems(data, int(input("Enter number of time you want to shift list: ")))
print(data)



