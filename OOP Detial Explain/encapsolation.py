# 3) Encupsolation( Capsole or Private karna ):-- Apni Class ka kuch Mathod or Attribute ko hum karti kha Private. Pavrite karni sa kya hoga ka koi B banda Usko direct access nahi kar sakta. Secound ka uss ko Access karni ka lya B koi Method hoga our Access karni ka lya B Method hoga.Exp:-- Facebook ko lya ka app message etc Dakti kha. Too wo kya kha Attribute's kha or Method. Too Private function ko Access karni ka lya B app ka pass "Geter Funtion" and Update kari ka lya app ka pass "Siter Funtion" hoti kha. Nam koi be rak sakti kha. Lekin scope Geter and Siter Funtion ka kha.


class Ca():
    def __init__(self,name,fname,age): #constractor
        self.__name = name # Attributies
        self.__fname = fname
        self.__age = age
# Yeh self.__name,fname,age ye Private value ho jata kha.
# Iss ko koi Access nahi kar sakta. Yeh sirf with in Class Accesable kha.
# Iss ka jo Responde kha wo iss Indentation ka ander kha Bahir nahi hoga.


    def disply_msg(self):
        return """
        ******** Disply Method ********

            Your name is:    {},
            Father name is:  {},
            Your Age is:     {}

        ********************************
        """.format(self.__name,self.__fname,self.__age)

    def SetValue(self,name,fname,age): # Yeh Value ko Update karni ka ly Create karahi kha. Is ko Setter kaha jata kha.
        self.__name = name
        self.__fname = fname
        self.__age = age
        print("""
        ***** Updateing Attributes *****
               
                Name:   {},
                F Name: {}
                Age:    {}   

        ***** Thank's for Updating *****
        """.format(self.__name,self.__fname,self.__age))

    def __hello(self): # Ye Pavrit kha. 
        return "Hello EveryOne Hahaha..!"
    
    
pi = Ca("Muzamil Shah","Ghulam Haider",32)
print(pi.disply_msg())
print(pi.SetValue("Shah Jehan","Wali Jan",45))
# print(pi.hello()) # Not can Access because this is Private attribute.
#  Iss ko B hum direct Access Nahi hota. Q ka ye Private kha.
# print(pi.__hello())# Also too not Access.
#  Iss ko B hum Class ka through Access kar sakti kha.
print(pi._Ca__hello()) # Private jo attribute ho ga. Iss ko hum is syntax ka through access kari gai.

# print(pi.name) # Not Accessing be thay can access in class.
# print(pi.__name) # Not Accessing be thay can access in class.
print(pi._Ca__name) # Can Access through Class na
