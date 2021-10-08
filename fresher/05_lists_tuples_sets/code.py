# list
l = ["Hoang", "Minh", "Le"]
# Can not modify in tuples
t = ("Bob", "Rolf", "Anne")
# Can not have duplicate element in set
s = {"Bob", "Rolf", "Anne"}

l[0] = "Smith"

l.append("Smith")

l.remove("Smith")

print(l)

s.add("Smith")

print(s)
