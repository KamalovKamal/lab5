# task 1

# class string():
#     def __init__(self):
#         self.str1 = input()

#     def print_String(self):
#         print(self.str1.upper())

# str1 = string()
# str1.print_String()

# task 2

# class Shape():
#     def __init__(self):
#         self.area=0
#     def area(self):
#         print(self.area)

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#         self.area = self.length * self.length
    
#     def printArea(self):
#         print(self.area)

# square = Square(4)
# square.printArea()

# task 3

# class Shape():
#     def __init__(self):
#         self.area=0
#     def area(self):
#         print(self.area)

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.lenght=length
#         self.width=width
#         self.area=self.lenght*self.width
    
#     def printArea(self):
#         print (self.area)

# rectangle = Rectangle(5,5)
# rectangle.printArea()
    
# task 4

# class Point():
#     def __init__(self,x=0,y=0):
#         self.x=x
#         self.y=y
    
#     def show(self):
#         # print(f"Point coordinates: ({self.x}, {self.y})")
#         print(f" ({self.x}, {self.y})")

#     def move(self, new_x, new_y):
#         self.x=new_x
#         self.y=new_y
    
#     def dist(self,new_x,new_y,x,y):
#         self.x=new_x-x
#         self.y=new_y-y
        

# point1 = Point(3, 4)
# point2 = Point(1, 1)
# point1.show()  
# point2.show()
# point1.move(5, 6) 
# point2.move(10, 12) 
# point1.show()
# point2.show()
# point1.dist(5,3,6,4)
# point2.dist(10,1,12,1)
# point1.show()
# point2.show()

# task 5

# class Account():
#     def __init__(self,first_name,last_name,position,balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.position = position
#         self.balance=balance

#     def deposit (self,balance,pluscash):
#         self.pluscash = pluscash
#         self.balance = balance + pluscash

    
#     def withdraw ( self, balance, minuscash):
#         self.minuscash = minuscash
#         if balance > minuscash:  
#             self.balance = balance - minuscash
#         else:
#             return ("ERROR")

# a = Account ('Kamal','Kamalov','bankir',100)
# a.deposit (100,50)
# print ("new balans after deposit = ", a.first_name,a.last_name,a.position,a.balance)
# a.withdraw(150,50)
# print ("new balans after witdraw = ", a.first_name,a.last_name,a.position,a.balance)

# b = Account ('Alibek','Ulitau','admin',1000000)
# b.deposit (1000000,500000)
# print ("new balans after deposit = ", b.first_name,b.last_name,b.position,b.balance)
# b.withdraw(1000000,800000)
# print ("new balans after witdraw = ", b.first_name,b.last_name,b.position,b.balance)

# c = Account ('Nurjan','Jannur','pr_agent',7777)
# c.deposit (7777,3333)
# print ("new balans after deposit = ", c.first_name,c.last_name,c.position,c.balance)
# c.withdraw(7777,1000000)
# print ("new balans after witdraw = ", c.first_name,c.last_name,c.position,c.balance)

# task 6
# Function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# # List of numbers to filter prime numbers from
# numbers = [2, 3, 5, 7, 10, 11, 13, 17, 20]

# # Use filter and a lambda function to filter prime numbers
# prime_numbers = list(filter(lambda x: is_prime(x), numbers))

# print("List of prime numbers:", prime_numbers)

