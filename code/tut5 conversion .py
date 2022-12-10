# type conversion 
a=12
x=2.3
x=x+a
print(x) 

# type casting 

a=293 
af=float(a)
print(a , af)
print(type(a),type(af)) # int float

b="1234"
bi=int(b)
print(b , bi)
print(type(a),type(af)) #str int 

boo=True
booi=int(boo)
print(boo,booi)
print(type(boo),type(booi))  # bool ,int 


#comments 

num=5 #this is single line comment 
'''' when you write the comment inside the triple quotes and this is 
    multiline comment 
'''
print(num)