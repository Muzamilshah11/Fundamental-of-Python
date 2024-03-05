
 # 1 Inheritance ( Warasat ):-- aur warasat hamesha Parent to Child muntaqil hota kha. OR Top to Buttom hoga.Example:-- Koi kahi ka yarr app ka jo awaz ha ye app ka grandfather(Dada) sa milta kha. NOW Ye jo chezzi Inherit kho app ka Walidan sa hoi ha.


# Concept of Inheritance So Let's Star:
class Ab():
    def __init__(self): # constractor 
        self.nationality = "Pakistan" 
        self.language = "Pushto"
        
    def speak(self,words): # Methods
        return  words

class Anotherone(Ab): # Inherit to Class name Anotherone
    pass
di = Anotherone()
print(di.language)
print (di.speak("Inheritance Simple Concept Using..!"))
print(di.nationality)


# Another example of Inheritance with Over Riding :
class Employee():
    def __init__(self,yname,fname,pay): # Constracter
        self.yname = yname # Attributs
        self.fname = fname
        self.pay = pay
        self.counter = 0
        
        # Method
    def disply_info(self):
        print(self.yname,self.fname,self.pay)

emp1 = Employee("Muhammd Shah", "Zubair Shah", 80000) 
emp2 = Employee("Muhamad Ishaq", "Muhammad Israr", 350000) 

# Instance OR Creating Object Variable 

print(emp1.disply_info())
print(emp2.disply_info())


# # Now the example of Inheritance and OverRiding Method
# # class Developer(Employee):-- Matlab Developer ka new class Bana raha ho iss koo connect karlo Employee wali Class sa. 
# # Employee me jetni B Parameter kha Wo super().__init__ command ka through Deduct karla ga. 
# #  Iss ko hum simple iss Tarah B kar sakti kha. syntax given below
# # class Developer(Employee):
# #               Pass . But Hum na new parameter Designation ki Zarort kha. Thoo iss lya Ye Baqi Code type karna parha.
class Developer(Employee): 
    def __init__(self,yname,fname,pay,designation): # Constracter
        super().__init__(yname,fname,pay) # Over Riding
#super().__init(  ):--  jo refer karta kha Apni Parent class ko. Matlab jab App na aik dapa constracter ma jo parameter's to pass kya ho. Thoo uss ko Dobara karni ki Zaroorat nahi Hoti. Bs Agr new parameter ki zaroorat ho to simple self.new_parameter_name thoo Asani sa ho jayga aur Porani parameter intalicance or recommedation auto yani super().__init__ ka through Catch kar laga.
        self.designation = designation
        print( """
        Developer Name: {},
        Father Name:    {},
        Developer Pay : {},
        Designation:    {}
        """.format(yname,fname,pay,self.designation))

# Class Inherit karin ka bad and Object or instance create karni ka bad Call karhi ki Zaroort yaha nahi kha.Iss ka Elawa Call karna ya Print karna zaroori kha.
dev_obj1 = Developer("Yar Muhammad", "Shah Khan", 2000000 , "AI Expert")
dev_obj2 = Developer("Shah Jehan", "Wali Shah", 5000000 , "IT Expert")
# print(dev_obj1)
# print(dev_obj1.disply_info())

    






    

