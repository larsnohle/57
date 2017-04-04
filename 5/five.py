s1 = input("What is the first number? ")
s2 = input("What is the second number? ")

i1 = int(s1)
i2 = int(s2)

string_to_output = "%d + %d = %d\n%d - %d = %d\n%d * %d = %d\n%d / %d = %d" % (i1, i2, i1 + i2, i1, i2, i1 - i2, i1, i2, i1 * i2, i1, i2, i1 / i2)
print(string_to_output)

#print("%d + %d = %d " % (i1, i2, i1 + i2))
#print("%d - %d = %d " % (i1, i2, i1 - i2))
#print("%d * %d = %d " % (i1, i2, i1 * i2))
#print("%d / %d = %d " % (i1, i2, i1 / i2))


