class calculator():
    def __init__(self,a,b,op):
        self.a=a
        self.b=b
        self.op=op
    def display(self):
        if(self.op=="+"):
            print(self.a + self.b) 
        elif(self.op=="-"):
            print(self.a - self.b) 
        elif(self.op=="*"):
            print(self.a * self.b) 
        elif(self.op=="/"):
            print(self.a / self.b) 
        else:
            print("Enter a valid operation")

a=input("Enter value of a: ")
b=input("Enter value of b: ")
op=input("Enter the operation to be performed: ")
a=float(a)
b=float(b)
operation=calculator(a,b,op)
operation.display()

# Sample output 1
# Enter value of a: 8
# Enter value of b: 7.5
# Enter the operation to be performed: *
# 60.0

# Sample output 2
# Enter value of a: 10
# Enter value of b: 5
# Enter the operation to be performed: +
# 15.0