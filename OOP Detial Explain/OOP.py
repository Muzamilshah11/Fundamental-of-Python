# # Today Topic: 1 Class, 2 Instance, 3 Method, 4 Attribute/Properties, 5 Class Variable, 6 Instance Variable, 7 Inheritance, 8 Polymorphisim , 9 Abstruction, 10 Encupsolation .
# # What is OOP:-- Stand for Object Orianted Programing:-- jis tarah real word mai chezo ko Yaad karni ka lya ya Manage karni ka lya Classification karti kha. Issi tarah ham apni program mai code ko Asani sa manage karni ka lya bilkul real world ki tarah hum OOP programing ka concept ko Istemal karti kah. First we will disscus Object.

# # What is Object:-- Har wo nam or Dunya ma wo Chezz jis ka koi name kha. Us ko hum Object kahti kha. Example : MObile , Man , School etc. Object hamesha 2 Chezzo par depend karta kha. 1 Method and 2 Attribute,

# # 1) Method:-- Har wo Chezz jo koi Action perfom karta ka called Method. Example: Bool sakta kha, Chal Sakta kha, Dakh Sakta kha, Soch Sakta kha.

# # 2) Attribute:-- Har wo chezz jis ka koi Properties ya Value hoti kha. OR Object ki koi B Haseyat ko Attribute kahti kha. Example: Name, Qualificaltion, Color, Size , Height, Weight,  etc.

# # OOP ki Zarorat Q Parhi:-- Farz kari agr hami pass 1000 object ho. Toh kya hum 1000 function banai ge? Iss kya iss sa bacni ka lya our time ko bachani ka lya hum sirf aik function bani ge Our 1000 object is aik function ko intelicence or recommendation ka through use kari ge.

# # 1 Inheritance ( Warasat ):-- aur warasat hamesha Parent to Child muntaqil hota kha. OR Top to Buttom hoga.Example:-- Koi kahi ka yarr app ka jo awaz ha ye app ka grandfather(Dada) sa milta kha. NOW Ye jo chezzi Inherit kho app ka Walidan sa hoi ha.

# # 2 Polymorpisim ( Aik Sa Zyada):-- Asa Koyi be Operater or Method jo aik sa Zyada kam perform kari is called polymorpisim. Example hum na Plus+ ka Operater ko dakha kha. Agr hum String ka sath lagyi to Concatination ka kam karta kha. Our Agr integer ka sath lagyi too addition perform hota kha. Too Plus+ ka Operater aik sa Zyada Behavier ko perform ka raha kha. Too ye app ka kya kha. Ye app ka Polimorpisim ki example kha.

# # i) Overloading(Function jo aik sa Zyada time banati kha):- Same Class ma koi B function jo app aik sa zyada time banati kha to Overloading hoga. Lekin iss ka apni 3 Sharti kha.
# # OR Same Class ma Same Function ko 2 dapa ya 3 dafa Repeat karna 

# # 1 Lekin iss ka same class me hoga. 
# # 2 funtion ka name same kha lekin 2,3,10 time bana kho kha. 
# # 3 ka iss ka number of parameter or sequence alg hoge.

# # ii)  Overriding(Dobara function banana):-- Funtion jo Parent Class sa inherit hojai Child Class mai Aur Wahi Function Hum Dobara Banoo Child mai iss ko overriding kahti ha.
# OR inheritance hum na parha ka Parant to Child mai inherit hoga.Speaking ka funtion Parant mai B kha our child ma B. Lekin inheritance honi ka bad Wahi hum Speaking ka function Dobara banati kha. Too iss ko kahti kha Overriding. Python ma Overriding ca concept nahi kha. Hum iss ko if elseif ka through bana sakti kha.

# # Parent sa Chlid ma inhert khowa aur uska oper app na wahi function dabara bana deya thoo ye howa Function Overriding.


# # 3) Encupsolation( Capsole or Private karna ):-- Apni Class ka kuch Mathod or Attribute ko hum karti kha Private. Pavrite karni sa kya hoga ka koi B banda Usko direct access nahi kar sakta. Secound ka uss ko Access karni ka lya B koi Method hoga our Access karni ka lya B Method hoga.Exp:-- Facebook ko lya ka app message etc Dakti kha. Too wo kya kha Attribute's kha or Method. Too Private function ko Access karni ka lya B app ka pass "Geter Funtion" and Update kari ka lya app ka pass "Siter Funtion" hoti kha. Nam koi be rak sakti kha. Lekin scope Geter and Siter Funtion ka kha.

# # 4) Abstruction(Uncomplite  Na Mukamal):-- Asi koi B Class jis ka directly instance or Object na ban saki Usko hum kahti kha Abstruction. Example Human class iss ka direct Object nahi ban sakta. Male class kha male class ka direct object ban sakta kha. Our Abstruct class ka tamam Method our Attribute ko access karni ka lya hum aik Child class banati kha. Our iss Child class mai hum iss ko inherit karti kha. Too inherit ka bad mai iss ko Access kar sakta kho.

# # Let's Stat
# class Man():

#     counter = 0 # Class Variable
#     def __init__(self,name,fname,course): # Constractor
#         self.name = name, # Attribute
#         self.fname = fname,
#         self.course = course,
#         Man.counter += 1 # calling Class variable
#         # print(Man.counter)
#         print("The name of {}, your father's name is {} and Apply for course {}. ".format(name,fname,course));

#     def Speaking(self, word = "Hello"): # Method
#         print("Hi and", word,"everyone!") 
    
#     def walking(self, speed = "10KM/H"): # Method
#         print("I am walking ", speed)

#     def eating(self,eat="Shami Kabab"): # Method
#         print("I am eating ",eat)

# obj1 = Man("Muzamil", "Haider", "A.I") # instance
# obj2 = Man("Saad", "Ismail", "A.I")
# obj3 = Man("Amar", "Ibrar", "A.I")
# # What is instance?
# # Jis Class ka Constracter Call kari wo us Class ka Instance HoGa.
# # obj1, obj2 aur obj3 konsi class ka instance kha?
# # obj11 Man Class ka instance kha.

# print(obj1.course)
# # print(obj1.name)
# # print(obj1.fname)
# # print(obj3.Speaking());
# # print(obj1.Speaking("Welcome"))
# print(obj2.eating())



# # Now apply Inheritance ( Warasat ):Simple Parant Class ko Child ma Inherit kya: Our Parant class ka sari Mathed's and Attribute's automaticlly Child Class ma add khoi.

# class Baba(Man): # Inherit to Parant's Class Man
#     pass
# ========================================
class Dog():
    
    def __init__(this,name,age):
        this.name = name,
        this.age  = age,
        
        print('The Dog name is:-- {},and Age is:-- {}'.format(name,age))

    def speak(this,word):
        return word+"...!"

c1 = Dog("Geman Shaper",11)
c2 = Dog("Gaky",10)

print(c1.name)
print(c2.name)
print(c1.speak("Bowh...bowh"))
update_age = c1.age = 14 # Update B karsakti kha.
print(update_age)


# ===============================================

# Inheritance(Warasat) Simple Example is given below:

# ================================
class A():
    def __init__(this,nationality,language):
        this.nationality = nationality
        this.language = language
    def speak(this,word):
        return word

class B(A):
    pass

object1 = B("Pakistani","Pushto")
object3 = B("UAE","Arbic")

print(object1.speak("I am speaking!"))
print(object3.nationality)
print(object3.language)




# # obj11 = Baba("Shahin Shah", "Akbar Ali", "A.I") 
# # # obj11 konsi class ka instance kha?
# # # obj11 Baba Class ka instance kha.

# # print(obj11.walking());
# # # print(obj11.eating("Chawal in Weeding Hall"))

# # print(Man.counter) # Class variable calling syntax when call anywhere.
# # print(obj1.eating())


# # class Dog():

# #     counter = 0; # Class Variable 

# #     def __init__(self, name, age): # Constractore
# #         self.name = name, # Attributes
# #         self.age  = age,
# #         Dog.counter = Dog.counter +1,
# #         print("This is {} and {} old. Total dogs are {}".format(name,age))

# #     # def break(self, word = " hi"):
# #     #         print(word)

# # Ob1 = Dog("German Shaper","10");
# # Ob2 = Dog("Asslition", "5");

# # print(ob1.age)

# class Car():

#     # counter = 0 # Class Variable
#     def __init__(self,made,model,year): # Constractor
#         self.made = made, # Attribute
#         self.model = model,
#         self.year = year,
#         # Man.counter += 1 # calling Class variable
#         # print(Man.counter)
#         print("The Model name is {}, Made by {} and the Model year is {}. ".format(model,made,year));

#     def Starting(self, start = "50 KM/H"): # Method
#         print("The Car is Starting With Speed is:--",start) 
    
#     def Stoped(self, speed="Now 0KM/H"): # Method
#         print("The Car is Stoped with Speed is:-- ",speed)


# obj1 = Car("HONDA", "CIVIC", 2023) # instance
# obj2 = Car("SUZUKI","ATLAS", 2020)       
# obj3 = Car("TOYTA","HYBRID", 2024)

# print(obj3.model)
# # print(obj2.year)
# print(obj1.Stoped())
# print(obj3.Starting())




















