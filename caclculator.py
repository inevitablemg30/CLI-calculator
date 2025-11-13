class Calculator():
    def __init__(self):
        self.num1 = int(input("Enter the first operand: "))
        self.num2 = int(input("Enter the second operand: "))
        
    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 ==0:
            return "ZeroDivison Error"
        return self.num1 / self.num2


print("The operations you can perform are :")
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
print("5:Exit")

while True:
    print("operands must be integers")
    user_input = int(input("Enter the number of the operation you want to perform :"))
    if user_input == 5:
        print("you have successfully exited from the cli calculator")
        break
    
    
    calc = Calculator()
    operations = {
        1:calc.addition(),
        2:calc.subtraction(),
        3:calc.multiplication(),
        4:calc.division()
        }
    

    if user_input in operations:
        print("answer is:", operations.get(user_input))
    
    else:
        print("The entered number is not correct please try again.")