# Today we will discuss the List[1) Method, 2)indexing, 3)Slicing(Important topic), (4)list Comprehensive, (5) loof, (6)for loof, (7) While loof, (8) Dictionary

# Difference about List and Array:-- List similer of Array liken not same of array Q K (1) Array ka jo Lenght kha Wo Fix hogi, (2) Array ma Hamisha Homogenis(mean's Tamam element ka data type same ho ge) data ho ga.

# List Mai data haitrogenis(mean's more then one datatype store kar sakti kha.)OR (mean's Tamam element ka data type change or Muhtalif ho ge).

# list:-- Means Akk he variable ma Multipule Value ko store karna jis ka datatype Alg Alg or change B kho sakta kha.

# Shello copy:-- jen ka address same kho.
# Deep copy:-- jen ka addres change kho.

l1 = ['Khan','Qasim','Ali',100,True,7.2]; # index Starting in O left to right Positive indexing and Right to Left to -1 Negitive indexing;
print(l1); # Now we are forword to indexing topic.
l1[2]= False; # Updating value by indexing.

l2 = [9,29,39,44,22,11,21];
print(sorted(l2)); # For Accending and operation #inline or #inmemory means Real data is not changing in Sorted function.
print(sorted(l2,reverse=True));# For Descending Operation  #inline or #inmemory
l2.sort(); # in memory mean's for update Real data.
print(l2);
print(id(l2)); # showing stor id location memory address

# Topic indexing
print(l1[1]); # left to right Positive indexing output is Qasim
print(l1[-1]);# Right to left Negetive indexing. output is 7.2
# We can update list element but Tuple con't update element

#  NOw we discuss pre-define-funtion like 'len','sorted',
print(len(l1)); # Showing total Element of List.
# print(sorted(l1))
# print(chr(l1));
# print(ord(l1));

# print(dir(list)); # ye shortcut show karta ka kisi be Object ka total Attributs(__class__,__add__,etc) and methods(append', 'clear', 'copy' etc).

# Small project about to add the name in list through append method.

# Using loof

# i = 0;# Stating index
# while i < len(l1): # Check logic with index range
#     print(l1[i]);
#     i +=1; #Increment / Decrement
# When using accending converting to Decending form then we are use
#     i= len(l1)-1;
#     while i >= 0:
#         print(l1[i]);
#         i -= 1;

#     names =[];
# while True:
#     a= input("Enter the Name:-- ");
#     if a!='x':
#         names.append(a);
#     else:
#         break
# print(names)

# for e in l1:
#     print(e);

# Generator function : range(start,end,step) 
# start = include 
# end = exculde
# setp = sequance

r1 = range(4);
for e in r1:
    print(e);  # Output [0,1,2,3
    

r2 = range(1,6);
for e in r2:
    print(e);   # Output [1,2,3,4,5]

r3 = range(0,60,10);
for e in r3:
    print(e); # Output [0,10,20,30,40,50]

    print(chr(65));
# ASCI CODE    (Amircon code for information interchange) Standard kha
# [0 - 9 => 48 sa 58 
#  A - Z => 65 sa 90   
#  a - z =>  97 sa 123 ]
cap = list(range(65,91))
print(cap);
for e in cap:
    print(chr(e));

# map funtion: list ka har aik element par formula lagana chahti kha tho map ka funtion use kari ga and  also called  Generated funtion (
print(list(map(chr,cap))); # Showing capital Alphabatic A to Z
names = ['kamal','Ahmad','shah','ali','khan']
print(list(map(len,names))); # Showing Total lenght of String
print(list(map(float,cap))); # Showing floating value
print(ord('z')); # Showing alpha letter to numaric number


# Slicing:-- Mean's more then one value Catch kar ka laoo. jab ka index only one value Catch kar ka laoo.
#  obj[start : end : step] Separate through colone ":"
# start : include
# end   : exclude
# step  : Sequence 

Slicing Example 
test_slicing = list(range(1,25))
print(test_slicing[0:22:3]);

test_string = ['Shah','Khan','Gull','Abbas','Musa khan','Saad','jibran','Amar'];
print(test_string[0:6:2])
 
s1 = list(map(chr,list(range(97,123))));
print(s1);
s2 = list(map(chr, list(range(65,91))))

print(*s2,sep=' '); # Mean's "*s2" matlab s2 ka har element ko alag alag print karo and "sep = ' '" iss sa kami's , hatadoo.

s3 = list(map(float, list(range(65,91))))

s4 = list(map(ord, s2));
s5 = list(map(chr,s4));



# print(list [::-1]);

# List Comprehensive :-- Comprehensive ka matlab ka app joo kam 1 sa zyada line mai karti kho. Uss ko short kar ka 1 aik line ma kari thoo iss ko hum kahti kha Comprehensive. Iss ka jo syntax kha wo if pa b apply kar sakti kha loof our list pa be apply kar sakti kha. Zyada log list comprehensive ko janti kha. Agr 6 Tuple comprehensive and also Dictionary comprehensive B kha.

# Below is Comprehensive 3 ways Syntax:
# for e in l1:    # e = element, l1 = list
#     print(e)    # statment
#2 if pa apply karti kha.
    # if logic:
    #     True value
    # else:
    #     False value

#3  True_value if logic else False_Value

a = 5
if a == 5:
    print("Pakistan");
else:
    print("China");

# Using 2nd way

b = 4

'TURKY'if b==4 else'CHINA'

# Statment for element in list
# [x for x in range(1,11)]
statment = list(x for x in range(1,4));
print(statment);

# Create Multiflication of any number
multiflication = list(x*2 for x in range(1,5));
print(multiflication);

# now we are generate table as you want
table = list("{} X {} = {}".format(2,x,x*2) for x in range(1,11));
for e in table:
    print(e);

# now we are using conditional and && or ||

for x in range(1,1001):# list of 1 to 1000
    if x%2==0 and x%5==0 and x%11==0:# condition all True then print.
        print(x); #given me Result if the above condition is ture .

# Example 2 
for x in range(1,100):
    if x%7==0 and x%12==0:
        print(x);

#  
print(dir(l1)[:35]);  # print(dir(l1)[:35]);# show me total Attribute with out method then help of slicing when both showing then only dir(l1);

# Using Append method.
print(l1);
l1.append("Shah khan"); # add the element of last of list.
print(l1);

# Using Count method.
a = "Pakistan Zinda bad";
print(a.count("a")); # to Count the spacific number or letter as you want

# Using Extend method.
a1 = [1,2];
b1 = [3,4];
print(a1,b1);
a1.extend(b1); # extend ka kam marge karna kha.
print(a1);

# Using Insert method.
l1.insert(0,'Kaleem khan');# insert ma hum aik spacific index mai value add kar sakti kha.
print(l1);

# Using Delete method.
del l1[4]; # Delete ka operation to perfom hota kha. liken koi value return nahi karta.
print (l1);

# Using POP method :-- Deleting the last elemet of list and can we show the result pop method.

ab = l1.pop(); # Value ko Delete or remove karta kha. Liken list ka end mai. Aur is ki value ko hum Show kar sakti kha. Aur index ka through be hum delete kar sakti kha like:-- l1.pop(0).


# Using remove method:-- Deleting the element by value

bc = l1.remove(7.2) # iss mai hum element of list ko remove karti kha by Value
print(l1);

# Using index method:-- index method hami show karta ka list ma jo element store kha uss ka index konsa kha.

index_no = l1.index('Qasim');
print(index_no);

# Using Enumerate method :-- is used to convert the list into tuple and showing both index with value like key value pairs.
enumerate_use = list(enumerate(l1)); # hami show karta kha index and value dono.
print(enumerate_use) 
# output [(0, 'Kaleem khan'), (1, 'Khan'), (2, 'Qasim'), (3, False), (4, True)]


# Using id method:-- Mehtod is showing variable storing address 

h = 4;
g = 4;
print(id(h));
print(id(g)); #output:-- 140724201780104

li = ['qasim', 'aslam', '03028858859','0092'];
print(li)
print(dict.fromkeys(li))# list ko dictionary ma convert karta kha.
print(dict.fromkeys(li,'abc'))
