# Today we will discuss the 3 main topic that is given below
# 1) Pre-Define Function:-- Repetation sa Bachni kalya Use karti kha.
    # Method:-- Action perform kari called method. Ex Dakna, Soona etc
    # Vs Attribute:-- Proferties or like Color, Width, Height etc

# 2) Operater's 3) Control Flow
#    ==============================================================
        ###########  Stating Now  ############

print("Sir Qasam");

a = "Pakitan";
print(a);
print(type(a));

# String Class Method and Attrinutes
    # Method:-- Action perform kari called method. Ex Dakna, Soona etc
    # Vs Attribute:-- Proferties or like Color, Width, Height etc

b = "Pakistan Zanda Bad";
print(b);
print(b.upper()); # Called intellicence OR recommendation also called #inline means Waqti tor per mujhi dekawo. Orgnal value ko change nahi kari ga.
print(b.title()); # String class ka total 42 attribute kha.
#print(b.capitalze()); total predefine funtion or intellicence is 42 attribute.
print(b.lower());
#help(print) Use for any funtion or mathed name help() between braceses.

# Static Code or Application :-- O code jo Programer khod Change kari thoo khe Change khoo Called Static Code VS DYNAMIC

abc = """
******  PIAIC   ****** 
Saylani Welfar Trust
Name : Muzamil Shah
Father's Name : Ghulam Haider
Roll No : 786
City: Peshawar
Country : Pakistan """

print(abc)
# Heard Code text or String Litterls both are same means

# Dynamic Code or Application :-- O code jo Programer khod Change Na kari. Bulki User khod Add or Change kari is Called Dynamic

name = "Qasim khan";
fname = "Muhammad Aslam";
city = "Karachi";

abcd = """
******  PIAIC   ****** 
Saylani Welfar Trust
Name : {}
Father's Name : {}
City: {}
"""
dynamic = abcd.format(name,fname,city);
print (dynamic)
# Funtion Types 2 types of funtion 1)Return Funtion 2)Non Return Funtion 
# Return Funtion:-- Iss ma jo bee Value or Result kho gha. Woo hum Variable mai Store kar sakti kha.  
#2)Non Return Funtion :-- Iss ka Value or Result ko hum Varable mai Store Nahi kar Sakti.

z = print("Called Non Return funtion");
print(z); # Why not printing in two time .

#x = input("Enter Your Name:") # Return Funtion
#print(x);

# Enter Value through input tag.
# name1 = input("Enter your Name Please:");
# fname = input("Enter Father's name Please:");
# city = input("Enter your City:");
# country = input("Enter your Country");
# relign = input("Enter your Relign ")

# xyz = """
# ******  PIAIC   ****** 
# Saylani Welfar Trust
# Name1 : {};
# Father_Name : {};
# City: {};
# Country: {};
# Relign: {};

# """
# Enter_data = xyz.format(name1,fname,city,country,relign);
# print(Enter_data);

#  Concatination Use now +
#  + Symbal value adding B karvata kha. Our Concatination B.
#  Iss lya iss ko  Operater Overloding B kaha jata kha.
a = 'Pakistan';
b = 'Zindabad';
print(a+b); # Concatination

c = 4;
d = 8;
print(c+d); # Addition 

# Operators {   Pemdas (Parentecis, Exponentional, Multiflication, Addition, Subtraction)
#:-- Computer ma jetni B kam perform hoti Us ko hum kahti Operation. Our Operation Perform hoti kha. App ka Operator ki waja sa. Operator Symbal hota kha like =,-,/,* etc
#                      
#   Mathmatics    :--  +,-,*,%,//,**           
#   Assign Operator:-- ==,+=,-=,/=,%=,*=,
#   Logical Operator:-- and &&, or ||                 }

# Mathmatics OPERATOR  :--  +,-,*,%,//,**  
print("\nMathmatics OPERATOR")
ab = 10;
bc = 2;
print(ab+bc);
# print(ab-bc);
# print(ab/bc);
# print(ab%bc);
# print(ab//bc);
# print(ab**bc);


# ASSIGN OPERATOR:-- ==,+=,-=,/=,%=,*=,
print("\nASSIGN OPERATOR")
a = 'China';
print(a *3); #Output  "ChinaChinaChina"

a += 'xyz';
print(a) #  Output  "Chinaxyz";
print("ASSIGN OPERATOR")

# COMPARISION OPERATOR:-- ==,<,>,<=,>=,!=,<>

print("\n COMPARISION OPERATOR:--")
print(5 == 5 ); # Equal to Output is :-- Ture
print(5 <= 5 ); # Less then or Equal to Output is:-- Ture
print(5 >= 5 ); # Grather then or Equal to Output is:-- Ture
print(5 != 5 ); # Not Equal to Output is:-- False
print(15 < 20 );# Output is Ture
print(5 > 3 ); # Output is Ture
print(" COMPARISION OPERATOR:\n");

#LOGICAL OPERATOR AND && OR |
print(" \n AND Syamble && :-- LOGICAL OPERATOR USING \n ")
print(5 == 5 and 6 <= 8 and 10 >= 9); # Must Every Condition is Ture 
print(5 == 5 & 6 <= 8 & 10 >= 19); # Then given him True otherwise False;

print("\n OR Syamble | :-- LOGICAL OPERATOR USING \n ")
print(5 == 5 or 6 <= 8 or 10 >= 19); # Atlest One Condition is Ture
print(5 == 10 or 6 <= 8 or 10 >= 29); # Then Given him True otherwise False;

# Concatination
a1 = 'xyz';
b1 = 'abc';
c1 = '27';
d1 = 22;
print(a1 + b1 + c1); # No Tenstion Because all data type is Same
print(a1,b1,c1);
# print(a1 + b1 + d1); # Error Generated because not all type is Same
# Now we use Typecasting:-- Akk Data type sa Dosri Data type ma Convert karni koo hum TypeCasting kahti kha. exp:-- str(),int() etc
print(a1 + b1 + str(d1)); # NOW Using TypeCasting Method

# cc = input("Enter your value 1  :-- ");
# dd = input("Enter your value 2  :-- ");

# print(cc + dd ); # For Concatination

# print(int(cc) + int(dd)); # For Addition

# CONTROL FLOW (LOOP(for , while )exception, if, else, elif) :-- Means to Control the Some thing or Statment
# if, else, elif;
    # if logic:
    #     True value
    # else:
    #     False value
    # 
            #  elif {
            #     if logic 1:
            #         Ture value
            #     elif logic 2:
            #         Ture value
            #     elif logic 3:
            #         True value
            #     else
            #         False Value
            # }

# name = input("Enter your name :-- ")
# if name.lower() == 'qasim': # for Case Sensetive use .lower() or .upper()
#     print("Hi Teacher");
# else:
#     print("Welcome Student");

# Creating Mark Sheet like percentage program

per = int(input("Enter Your Obtain Marks out of 100 :-- "))

if  per>=0 and per<33:
    print("Sorry Your Are Fail! Try Again");
elif per>=33 and per<40:
    print ("Grade F");
elif per>=40 and per<50:
    print("Grade E");
elif per>=50 and per<60:
    print("Grade D");
elif per>=60 and per<70:
    print("Grade C");
elif per>=70 and per<80:
    print("Grade B");
elif per>=80 and per<90:
    print("Grade A");
elif per>=90 and per<=100:
    print("Grade A+")
else:
    print("Invalid Number");



# import this 
# :-- The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!















