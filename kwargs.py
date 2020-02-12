def showDetails(**kwargs):
    for key, value in kwargs.items():
        if key == "name":
            print(f"Hello {value}")
        if key == "klass":
            print(f"Here is your result for the class of {value}")
        if key == "marks":
            print("Your scorecard is as follows:")
            print("ClassMarks:")
            total = 0
            max = 0
            min = 100
            ma = ""
            mi = ""
            for key, value in kwargs[key].items():
                print(f"{key} : {value}")
                total += value
                if value > max:
                    max = value
                    ma = key
                if value < min:
                    min = value
                    mi = key
            print(f"Total Marks are: {total}")
            print(f"Percentage is as follows: {round(total/400*100, 2)}%")
            print(f"Maximum marks are in {ma}")
            print(f"Minimum marks are in {mi}")
        if key == "nextClass":
            if value == True:
                print("You are promoted to next class")
            else:
                print("Work hard and try again")

                

# variable class changed to klass as class is python keyword/ reserved word
showDetails(name = "Ali", klass = "AI", marks = {"math" : 50, "physics" : 80, "biology" : 90, "computer" : 67}, date = "1 Feb 2020", nextClass = True)
