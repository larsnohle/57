# Four
noun = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter a adjective: ")
adjective2 = input("Enter another adjective: ")
adverb = input("Enter a adverb: ")

# Do you walk your blue dog and your green cat quickly? That's hilarious!
string_to_output = "Do you %s your %s %s and your %s %s %s? That's hilarious!" % (verb, adjective, noun, adjective2, noun2, adverb)

print(string_to_output)
