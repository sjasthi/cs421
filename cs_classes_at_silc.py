# Representation for th eentire SILC.
# This has a list of CS Classes
# Where "CS_Class" is another class
class SILC:
    def __init__(self, list_of_classes):
        self.list_of_classes = list_of_classes
      
      
    def __repr__(self):  
       return 'SILC(list_of_classes=%s)' % (self.list_of_classes)
    
    def __str__(self):  
       return 'SILC(list_of_classes=%s)' % (self.list_of_classes)
   
   
    # Returns the count of students in all the classes    
    def count_students(self): 
        # Loop through entire SILC cs classes list
        # find the count of students in each class
        total = 0
        for cs_class in self.list_of_classes:
            count = len(cs_class.list_of_students)
            total = total + count
        #return the total
        return total
            
        
# Representation for one CS Class
# This has a list of students 
# Where "Student" is another class
class CS_Class:
    def __init__(self, list_of_students):
        self.list_of_students = list_of_students
      
    def __repr__(self):  
       return 'CS_Class(list_of_students=%s)' % (self.list_of_students)
    
    def __str__(self):  
       return 'CS_Class(list_of_students=%s)' % (self.list_of_students)
      

# Representation for one Student
# A student has a name, email and a computer 
# Where "Computer" is another class      
class Student:
    def __init__(self, name, email, computer):
        self.name = name
        self.email = email
        self.computer = computer
  
    def __repr__(self):  
       return 'Student(name=%s, email=%s, computer=%s)' % (self.name, self.email, self.computer)
    
    def __str__(self):   
       return 'Student(name=%s, email=%s, computer=%s)' % (self.name, self.email, self.computer)
    
       

# Representation for a Computer      
class Computer:
    def __init__(self, model, type, cost):
        self.model = model
        self.type = type
        self.cost = cost
  
    def __repr__(self):  
       return 'Computer(model=%s, type=%s, cost=%s)' % (self.model, self.type, self.cost)
    
    def __str__(self):  
       return 'Computer(model=%s, type=%s)' % (self.model, self.type)

#-----------------------------
# all the test data (classes and objects) are created here
#-----------------------------
       
#create an instance of computer
computer_1 = Computer("Dell", "Windows", 1000)
# print(computer_1)

#create an instance of computer
computer_2 = Computer("HP", "Windows", 300)
# print(computer_2)


#create an instance of computer
computer_3 = Computer("Apple", "MAC", 1200)
# print(computer_3)


#create a student 1
student_1 = Student("Ishana", "ishana@gmail.com", computer_1)
# print(student_1)

#create a student 2
student_2 = Student("Happy", "happy@gmail.com", computer_3)
# print(student_2)


#create a student 3
student_3 = Student("Vishnu", "vishnu@yahoo.com", computer_3)
# print(student_3)



# Create a python class
python_students = [student_1, student_2, student_3]
python_class = CS_Class(python_students)
# print(python_class)



# Create a PHP class
# In the interest of time, I am assuming that the same students are in both the classes
# We should create new students (TBD)
php_students = [student_1, student_2]
php_class = CS_Class(php_students)
# print(php_class)

#Create the entire SILC universe
# which is consisting of several CS Classes
list_of_classes = [python_class, php_class]
silc_2020_21 = SILC(list_of_classes)
# print(silc_2020_21)

# Now get the total count of the students in all CS Classes at SILC

total_count_of_students = silc_2020_21.count_students()
print("Entire SILC --> ", silc_2020_21)
print("Total Count of Students ", total_count_of_students)

