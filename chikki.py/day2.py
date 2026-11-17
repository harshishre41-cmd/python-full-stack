# for i in range(50);
#     print("good morning teacher!")


#     i = 1
#     while i <=5:
#     print("Good morning students!")
#      i += 1   

# def great():
#     print("hello students")
#     print("welcome to python programming")
# great()

#  def add(a,b):
#     result = a + b
#       print(result)
#   add(18,20)
#   add(50,30)

# students=["nibba","nibbi","dinga","dingi"]
# print(students[3])
# print(students)

# students = ["nibba","nibbi","Dinga","Dinge"]
# students.append("punga")
# students.remove("Dinga")
# students.insert(1, "Dinga")
# print(students)

#########Tuple##########

# student_details = ("nibba", 23,85.5,True)

# print(student_details[0])
     
     ##############Dictonary#############
# student= {  
#     "name": "nibba",
#     "age": 23,
#     "marks":85.5,
#     "passed": True
# }
# student["course"] = "python programming"
# student["marks"] = 90
# print(student["name"],)
# print(student["course"])
# print(student["marks"])

   ###########Class & object############

# class student:
#      def display(self):
#          print("hello students")
#          print("welcome to python programming")
# s1 =  student()

# s1.display()

#################Constructor#################

# class student:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)

# s1 = student("nibba", 23, 85.5)
# s2 = student("nibbi", 22, 90.0)
# s1.display()
# s2.display()

# 
# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set marks(self, marks):
#         self.__marks = marks

#     def show_marks(self):
#         print("student marks:", self.__marks)

#         s1 =student()
#         s1.set_marks(85.5)
#         s1.show_marks()

# class grandfather:
#     def land(self):
#         print("grandmother has a land ")

# class mother(grandfather):
#         def house(self):
#             print("mother has a house")

# class son(mother):
#         def car(self):
#             print("son has a car")

# s = son()
# s.land()
# s.house()            
# s.car()
 
 ##########abstract class##############
   
from abc import ABC, abstractmethod

# class payment (ABC):
#      @abstractmethod
#      def pay(self, amount):
#         pass

# class UPI(payment):
#     def pay(self, amount):
#         print(f"Paid (amount) using UPI")

# class Card(payment):
#     def pay(self, amount):
#         print(f"paid (amount) using Card") 

# p1 = UPI()
# p2 = Card()
# p1.pay(1000)
# p2.pay(2000)      
