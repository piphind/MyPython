monday_temparatures = [9.1, 8.8, 7.5]

print(monday_temparatures)

monday_temparatures.append(8.8)

print(monday_temparatures)

print("The index of value '8.8' is ", monday_temparatures.index(8.8))

monday_temparatures.pop(-1)

print(monday_temparatures)

monday_temparatures.pop(-1)

print(monday_temparatures)

monday_temparatures.pop(-1)

print(monday_temparatures)

monday_temparatures = [9.1, 8.8, 7.5, 6.6, 9.9]

print(monday_temparatures)

print("The first item in the list is ", monday_temparatures.__getitem__(0))
print("The first item in the list is ", monday_temparatures[0])
print("Here is a selection of monday's temperatures (a slice)", monday_temparatures[1:4])
print("Here is another selection of monday's temperatures (a slice)", monday_temparatures[:4])
print("And another selection of monday's temperatures (a slice)", monday_temparatures[3:])

print("And here is a selection of monday's temperatures (a slice) using negative (-) indices", monday_temparatures[-2:])

monday_temparatures.clear()

print(monday_temparatures)




