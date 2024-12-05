# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1) 

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val)

data = bytearray(b'hello , world!')
view = memoryview(data) 
print(view)

import array
arr = array.array('i',[1,2,3 ,4,5])
view = memoryview(arr)
print(view)
