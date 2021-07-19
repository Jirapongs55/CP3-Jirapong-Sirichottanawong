def aggregate(operator,round):
    sum =  0
    diff = 0
    mult = 1
    div = 1
    if operator == "+" or operator == "sum" :
        for i in range(round):
            inputNumber = int(input("Input X("+str(i+1)+") : "))
            sum = sum + inputNumber
            continue
        print("Sum : "+str(sum))
    elif operator == "-" or operator == "diff" :
        for i in range(round):
            inputNumber = int(input("Input X("+str(i+1)+") : "))
            diff = inputNumber - abs(diff)
            continue
        print("Diff : "+str(diff))
    elif operator == "x" or operator == "*" :
        for i in range(round):
            inputNumber = int(input("Input X("+str(i+1)+") : "))
            mult = mult*inputNumber
            continue
        print("Multiply : "+str(mult))
    elif operator == "/" or operator == "div" :
        for i in range(round):
            inputNumber = int(input("Input X("+str(i+1)+") : "))
            div = inputNumber/div
            continue
        print("Div : "+str(div))
aggregate("-",3)












































































