 # 4) Abstruction(Uncomplite  Na Mukamal):-- Asi koi B Class jis ka directly instance or Object na ban saki Usko hum kahti kha Abstruction. Example Human class iss ka direct Object nahi ban sakta. Male class kha male class ka direct object ban sakta kha. Our Abstruct class ka tamam Method our Attribute ko access karni ka lya hum aik Child class banati kha. Our iss Child class mai hum iss ko inherit karti kha. Too inherit ka bad mai iss ko Access kar sakta kho.
#  OR Abstruction:-- Class which contains one or more abrstruc Methods.
# Abstract Method :-- A metod that can Declaration but does not have an implementation 

# Concept of Example or Syntax of Abstruction Method

# from abc import ABC, abstruction
# class Human: # Assign Class Name Without Braces() this is Role:
# # Abstruction Class banati waqt () bracess ki zarort nahi hoti

#     # @abstruction # Called is Decorater
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age

#     def making_noise(self):
#         return "Hahaha......!"

# class Man(Human):

#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
#         print("Your Name {} and you are {} Year's Old".format(self.name,self.age))


# p1 = Man("KHAN",22)
# print(p1.name)
# print(p1.age)
# print(p1.making_noise())


class Vehicle():
    def go(self):
        pass
# Abstract Method:-- A metod that can Declaration but does not have an implementation 

class Car(Vehicle):
    def go(self,word = "We drive the Car" ):
#  word ko Yaha B vale assign howa kha. Aur function calling ka time be New Value Lata kha.Aur jo Value Assign howa hota kha too woo Skip hota kha aur New value ko Add karta kha. Jab ka aur Syntax mai kam nahi karta. 
# Example :-- car.go("newvalue")
        return word

    def stop(self):
        print("This Car are Stop.")

class MoterCycle(Vehicle):
    def go(self):
        print ("We drive the MoterCycle...!")

    def stop(self):
        print("The MoterCycle is Stop Now!")

# Creating Instance or Object's
moter = MoterCycle() 
car = Car()

print(car.go("Driving With Family"))
print(moter.go())
print(car.stop())
print(moter.stop())


