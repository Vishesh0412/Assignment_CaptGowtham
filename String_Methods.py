Text = "may the force be with you"
x = Text.capitalize()
print(x)

Text = "May the force be with you"
x = Text.casefold()
print(x)

Text = "May the force be with you"
x = Text.center(8)
print(x)

Text = "May the force be with you"
x = Text.count("force")
print(x)

Text = "May the force be with you"
x = Text.encode()
print(x)

Text = "May the force be with you"
x = Text.endswith(".")
print(x)

Text = "May the force be with you"
x = Text.expandtabs(5)
print(x)

Text = "May the force be with you"
x = Text.find("be")
print(x)

Text = "May the {force} be with you"
print(Text.format(force = "sheldon"))

Text = "May the force be with you"
x = Text.index("force")
print(x)

Text = "May the force be with you"
x = Text.isalnum()
print(x)

Text = "May the force be with you"
x = Text.isalpha()
print(x)

Text = "May the force be with you"
x = Text.isdigit()
print x

Text = "May the force be with you"
x = Text.isdecimal()
print x

Text = "May the force be with you"
x = Text.isidentifier()
print(x)

Text = "May the force be with you"
x = Text.islower()
print(x)

Text = "May the force be with you"
x = Text.isprintable()
print(x)

Text = "May the force be with you"
x = Text.isspace()
print(x)

Text = "May the force be with you"
x = Text.istitle()
print(x)

Text = "May the force be with you"
x = Text.isupper()
print(x)

Text = ("Peter", "Ninja Hattori")
x = "#".join(Text)
print(x)

Text = ("Peter Parker")
x = Text.ljust(10)
print(x, "is one of my favourites")
