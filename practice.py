names = ["Reuben","Brady","Ellie","Annalise","Addie"]
print(names)

#del names[0]
#print(names)
names.remove("Reuben")
print(names)

names.append("Meghan")
print(names)

for name in names:
    print(f"{name} is at my table")

#names.reverse()
#print(names)
names.sort(reverse=True)
print(names)