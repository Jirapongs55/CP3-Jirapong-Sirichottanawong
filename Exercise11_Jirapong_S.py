inputNumber = int(input("Input the pyramid level : "))
blankText = " "
text = input("Input the character for pyramid monomer : ")
for i in range(inputNumber):
    print(blankText*(inputNumber-(i+1)),end=text*((2*i)+1))
    print(blankText*(inputNumber-(i+1)))
print("-"*12,"The End","-"*12)

'''
# Pattern
print(" "*2,end="*")
print(" "*2)
print(" "*1,end="***")
print(" "*1)
print(" "*0,end="*****")
print(" "*0)
'''





















































