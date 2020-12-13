
f = open("list.txt")
numbers = f.readlines()
print(numbers)

for x in numbers:
  for y in numbers:
    for z in numbers:
      if int(x)+int(y)+int(z) == 2020:
        print (int(x),int(y),int(z),int(x)+int(y)+int(z),int(x)*int(y)*int(z))




