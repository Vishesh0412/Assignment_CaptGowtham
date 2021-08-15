#List Methods

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.append("Dexter")
print(Mylist) #This pogram adds one item at the end

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.clear()
print(Mylist) #This program clears the list

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
y = Mylist.copy()
print(y)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
x = Mylist.count("Batman")
print(x)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Workout = ["Cycling", "Running", "Pushups"]
Mylist.extend(Workout)
print(Mylist)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
x = Mylist.index("Vishesh")
print(x)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.insert(2, "Superman")
print(Mylist)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.pop(2)
print(Mylist)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.remove("Shawshank Redemption")
print(Mylist)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.reverse()
print(Mylist)

Mylist = ["Shawshank Redemption", "Batman", "1", "Vishesh"]
Mylist.sort()
print(Mylist)
