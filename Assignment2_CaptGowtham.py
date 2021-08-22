#Problem 1 (While and For Loop- Break and Continue)

i = 9
while i > 0:
    print(i)
    i = i - 1
    #Discontinues at 5
    if i == 5:
        break

i = 9
while i > 0:
    i = i - 1
    #This skips the value 6
    if i == 6:
        continue
    print(i)

#Problem 2 (For Loop Star Pattern)

def pattern(n):
    k = n - 1
    for i in range(0,n):
        

#Problem 3 (Dictionary Methods)
computer = {
     "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
computer.clear()
print(computer)

#Method 2
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
x = computer.copy()
print(x)

#Method 3
x = ('key1', 'key2', 'key3')
y = "computer"

mydict = dict.fromkeys(x,y)
print(mydict)

#Method 4
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
x = computer.get("brand")
print(x)

#Method 5
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
x = computer.items()
print(x)

#Method 6
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
x = computer.keys()
print(x)

#Method 7
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
computer.pop("graphics")
print(computer)

#Method 8
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
computer.popitem()
print(computer)

#Method 9
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
x = computer.setdefault("brand")
print(x)

#Method 10
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
computer.update({"brand": "HP"})
print(computer)

#Method 11
computer = {
    "processor": "intel",
    "graphics": "nvidia",
    "brand": "dell"
}
x = computer.values()
print(x)
