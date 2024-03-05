# # Dictionary:-- Similar to objecet(key:value pairs) also discauss about methods, attributes and extract value from dictionary.

# li = ['qasim', 'aslam', '03028858859','0092'];
# print(li)
# print(dict.fromkeys(li))# list ko dictionary ma convert karta kha.
# print(dict.fromkeys(li,'abc'))# none ka jagha apna value put karna kho.
# list_convert_to_dictionary = dict.fromkeys(li)
# print(dict.fromkeys(li,'any value as you want'))


# # all elements are stored with index number
# # 0 = name
# # 1 = father_name
# # 2 = cell
# # 3 = country code 
# # print(li[0],li[1],li[2],li[3]) # Print or Catch through index
# # we can print another way that's can explane give below
# # print(*li); 
# # hum aghr list ma value put karti waqat agar name ka jagha pa father name put kari or cell ka jagha agar country kari to error ka chancess zyada kha. Agar 6 Dictionary ma yeh issues solve ho jati kha. Q k Dictionary ma key,value pair(joreh) hoti kha.

# # Dictionary ki zarorat Q ayee Q K all rady hum list Use kari kha?
# # Ans:-- Q K hum list koye value catch karti kha to indexing ka through kari kha. Iss lya hami dictionary ki zarorat pari. Q K Dictionary ma ham value ko key ka through access or catch karti kha. Exaple given below:



obj1 = {
#  element = Key:Value (Pair)
# key      = String , Integer 
    'name' : 'Muzamil Shah',
    'Fname' : 'Ghulam Haider',
    'cell' : '03028858859',
    'id' : '0092',
    'age': '30',
   '0' : 'Pakistan Zinda Abad',
   ('abc'): 'Hello World', # Can Support Tuple value but not support list type data. 
    # ['def']: 'NOt Supporting list type',
    'check' : [1,2,3,4,5,6] ,# Value side can support all type of data but key side only support string type and integer type,
}
# # print(obj1);
print(obj1.keys());

list1 = obj1.keys(); # Dictionary ka key ko hum list ma store kar sakti ha.
# Creating simple program that's check your key are ture
# for x in list1:
#     if x == "check":
#         print("True Value ");
   
      
# print(obj1.values());
# print(obj1.get('any key'))# get ka through hum apni program ko crash honi sa ba6ati kha. Agr key object ma mojod B na ho to be Error show nahi kari ga. OR print(obj1.get('any key','Not valid value'))
# print(obj1['check'][0]) # chatching through indexing
# print(obj1['check'][1])

 # print(obj1['name']);
 # print(obj1['Fname']);
 # print(obj1['cell']);
 # print(obj1['age']);
 # print(obj1['0']);# This is key not a index number

#  Dictionary ko hum Tuple ma covert kar sakti kha
dic_covert_tuple = obj1.items();
print(dic_covert_tuple);# dic converting to Tuple format. 

for k,v in obj1.items():    
    print("Key = ",k," Value = ",v);

# Dictionary Mathods:-- 
# dict.clear()
# dict.keys()
# dict.values()
# dict.items()# to convert the dict to tuple format
# dict.pop('abc')# return value
# dict.popitem()# return kari last key and value
# dict.setdefault('xyz', 'pak'); yeh real data update karta kha. ye same .get() ka kam karta kha.
# dict.update(newdata) # newdata = {'a':'A','b':'B'}, obj1.update(newdata) Real data update and change hoga.







 






