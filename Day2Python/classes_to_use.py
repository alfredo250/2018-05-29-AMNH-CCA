class operateOnTwoNumbers :
    def __init__(self,  num1, num2, operation='division'):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation
        
    def divide_me(self):
        return self.num1/self.num2
    
    def multiply_me(self):
        return self.num1*self.num2
    
    def subtract_me(self):
        return self.num1-self.num2
    
    def execute_operation(self):
        if self.operation == 'division':
            return self.divide_me()
        elif self.operation == 'multiplication':
            return self.multiply_me()
        elif self.operation == 'subtraction':
            return self.subtract_me()
        else :
            print "invalid operation"
