# Four
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter a adjective: ")
adverb = input("Enter a adverb: ")

#Do you walk your blue dog quickly? That's hilarious!
string_to_output = "Do you %s your %s %s %s? That's hilarious!" % (verb, adjective, noun, adverb)

print(string_to_output)
