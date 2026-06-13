class student :
    school = "Delhi Public School"
    @classmethod
    def show__school(cls) :
        print(cls.school)

student.show__school()

class calculator :
    @staticmethod
    def add(a,b) :
        return a+b
    
print(calculator.add(5,3))

class student:
    school = "Delhi Public International School"
    @classmethod
    def show_school(cls) :
        print(cls.school)

student.show_school()

class Math :
    @staticmethod
    def multiplication(a,b) :
        return a*b
    
print(Math.multiplication(2,6))

class Temperature :
    @staticmethod
    def celsius_to_fahrenhein(c) :
        return(c*9/5)+32

print(Temperature.celsius_to_fahrenhein(25))

       