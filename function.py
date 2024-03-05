# Function:-- Real life ma B Repetation sa bachni ka lya hum function use karti kha. 
    
# Example :-- Hum tea ka example dati kha. Agar hum kisi bandi ko 6ai banani ko kahi too sath ma kahi ka Pati,Shugar aor mailk lya. aur pani mai gharam kari aur filter kar ka Cup ma dali. Bar bar repatation sa bachni ka lya hum function banati kha.

# Function hamesha 2 type ka hogi. 
# 1) Return funtion:-- Jo hami kuch return kari. Jis ki value hum variable mai Store kar sakti kha.
#  2) Non return funtion:-- Jis ki value hum Store nahi kar sakti.

# Default funtion:-- Aisa function jo apsy koi argumet na ly called default

# function Syntax: [Function declaration(name)(parameters) , Fun Body(Statment, karna kya kha.), Fun Calling(jab zarorat pari ge to call kari ge.) ]
# Function ma Variable banati waqat parameter and Call karti waqat Argument

# def name(parameter1, parameter2): Function declaration 
        # statment1
        # statment2     Funtion Body
        # statment3
    # name(argument,argument2)value dana ho ga. Funtio calling
# ========= Without Parameters and Argument's ==========
x = 'Awesome';
def abc():
    print("Hello Word " + x)
abc()

# ==================== With Parameter's and Argument's =============
def sum(value1,value2):
    return value1 + value2; # return function mean's the value that can store in variable. 
print(sum(123,123)); 
print(sum(12,10));

# =======================================================
# Seqencetial argumet :-- Simple 1st is 1st and last is last
#  Required Argument's program
def student(name,fname,cell):
    # print("Your Name is:-- " + name)
    # print("Your Father name is:-- " + fname)
    # print("Your Cell no :-- " + cell)

        enter   = """
        Saylani Welfare Trust
        University Town Pehsawer 
        Your name : {}
        Father name: {}
        Cell no : {} """.format(name,fname,cell)
        return enter
  # The parameter and argument's are must equal if not equal they are not executable or not runing in terminal  
print(student('Khan','Abdul Wali','0300-2345678'))
print(student('Ali khan','Wali khan','0311-2345678'))


# def abc(**a): # not working
#     print(**a);
# print(abc(name = 'khan', fname = 'Wali khan'))

def bcd(*a):
    return sum(*a);
print(bcd(12,22));

   
