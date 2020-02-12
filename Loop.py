
data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
'''
if "python" in data:
    print("Python is present")
if "html" in data:
    print("HTML is present")
if "c" in data:
    print("c is present")
'''
def checkVal(lis):
    for i in lis:
        if i == "python":
            print("Python is present")
        if i == "html":
            print("HTML is present")
        if i == "c":
            print("c is present")
            
checkVal(data)

