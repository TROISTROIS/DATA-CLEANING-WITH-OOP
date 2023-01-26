## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
my_set = {2, 3, 5}
print(type(l))
print(type(s))
print(type(d))
print(type(my_set))

## 2. Sets ##

tri_num_sequence = [1, 3, 6, 10, 15, 10, 6, 3, 1]
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
trinum_5 = set(tri_num_sequence)
print(trinum_5)
odd_20 = set()
for i in range(20):
    if i%2 != 0 :
        odd_20.add(i)
print(odd_20)
odd_trinum = set()
for i in trinum_5:
    if i%2 != 0:
        odd_trinum.add(i)
print(odd_trinum)

## 4. Defining a Class ##

class NewList():
    pass

## 5. Instantiating a Class ##

class NewList(DQ):
    pass
newlist_1 = NewList()
print(type(newlist_1))

## 6. Creating Methods ##

class NewList(DQ):
    def first_method():
        return "This is my first method"
newlist = NewList()
                  
    

## 7. Understanding 'self' ##

class NewList(DQ):
    def first_method(self):
        return "This is my first method"
newlist = NewList()
result = newlist.first_method()
print(result)

## 8. Creating a Method That Accepts an Argument ##

class NewList(DQ):
    def return_list(self, input_list):
        return input_list
newlist = NewList()
result = newlist.return_list([1,2,3])
print(result)

## 9. Attributes and the Init Method ##

class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state
my_list=NewList([1,2,3,4,5])
my_list.data

## 10. Creating an Append Method ##

# The NewList definition from the previous
# screen is copied here for your convenience

class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state
    def append(self, x):
        self.data = self.data + [x]
my_list = NewList([1,2,3,4,5])
print(my_list.data)
my_list.append(6)
print(my_list.data)

        

## 11. Creating and Updating an Attribute ##

class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()
    def calc_length(self):
        length = 0
        for item in self.data:
            length += 1
        self.length = length
    def append(self, x):
        self.data = self.data + [x]
        self.calc_length()
    def calc_length(self):
        length = 0
        for item in self.data:
            length += 1
            self.length = length

fibonacci = NewList([1,1,2,3,5])
print(fibonacci.data)
print(fibonacci.length)
fibonacci.append(8)
print(fibonacci.data)
print(fibonacci.length)