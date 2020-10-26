from random import randint
Zephyr = [["Dan Allenby", False], ["Ravi Shankar", False], ["Prahlad Swamy", False],
          ["Mark Gaywood", False], ["Mel Cooper", False], ["Yemi Lalude", False],
          ["Paul Wallis", False], ["Theo Brown", False], ["Herwig Mueller", False],
          ["David Brighton", False], ["Priya Nair", False],
          ["John LeDrew", False], ["Jon Penny", False]]

i = 1

print("STANDUP Rota")
print("============")
print()

while i < 14:
    ind = randint(0, 12)
    if Zephyr[ind][1] is False:
        if i < 10:
            txt = "  {}) {}"
        else:
            txt = " {}) {}"
        print(txt.format(i, Zephyr[ind][0]))
        Zephyr[ind][1] = True
        i = i + 1

print()
print(" 14) Caroline Apicella")
print(" 15) Tricky Davies")
print(" 16) Mike Manchee")
print(" 17) Dan Gittins")
print()
print(" 18) Phil Hind")
print()
done = input(" Done")
