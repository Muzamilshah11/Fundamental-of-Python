 # 2 Polymorpisim ( Aik Sa Zyada):-- Asa Koyi be Operater or Method jo aik sa Zyada kam perform kari is called polymorpisim. Example hum na Plus+ ka Operater ko dakha kha. Agr hum String ka sath lagyi to Concatination ka kam karta kha. Our Agr integer ka sath lagyi too addition perform hota kha. Too Plus+ ka Operater aik sa Zyada Behavier ko perform ka raha kha. Too ye app ka kya kha. Ye app ka Polimorpisim ki example kha. Iss ka 2 type's kha.

# i) Overloading(Function jo aik sa Zyada time banati kha):- Same Class ma koi B function jo app aik sa zyada time banati kha to Overloading hoga. Lekin iss ka apni 3 Sharti kha.
# OR Same Class ma Same Function ko 2 dapa ya 3 dafa Repeat karna 
# python me overloading hoti nahi kha. But hum iss ko if else  ka through kar sakti same syntax or simple method ka.

# 1) Lekin iss ka same class me hoga. 
# 2) funtion ka name same kha lekin 2,3,10 time bana kho kha. 
# 3) ka iss ka number of parameter or sequence alg hoge.

# ii) Overriding(Dobara function banana):-- Funtion jo Parent Class sa inherit hojai Child Class mai Aur Wahi Function Hum Dobara Banoo Child mai iss ko overriding kahti ha.
# OR  inheritance hum na parha ka Parant to Child mai inherit hoga.Speaking ka funtion Parant mai B kha our child ma B. Lekin inheritance honi ka bad Wahi hum Speaking ka function Dobara banati kha. Too iss ko kahti kha Overriding. Python ma Overriding ca concept nahi kha. Hum iss ko if elseif ka through bana sakti kha.

# Parent sa Chlid ma inhert khowa aur uska oper app na wahi function dabara bana deya thoo ye howa Function Overriding.

# Concept of Over Riding Example Let's Star:

class A():
    def __init__(self): # Creating Constractor 
        print("Parent's Class")

    def speaking(self): # Creating Method:
        print("Hi! and hello.. We are with Parent's...!")

class B(A):
    def __init__(self): # Over Riding
        self.words=None # Mean's Previous statment or Words None Print me! 
        print("Child Class")

    def  speaking(self): # Over Riding
        print("Hi! I am Child Class")

tellme = B() # inherit with Class A that is Parent Class.
print(tellme.speaking()) # Now Print Method Speaking()

tellme_parent = A()
print(tellme_parent.speaking())
    



