
obi_wan_quotes = ["These aren't the droids you're looking for."]
ceasar_quotes = ["Veni, vici, vidi.", "Alea jacta est."]
hedge_quotes = ["It is a bridge, and you know what we do to bridges, don't you?"]
mael_quotes = ["Now get your hands off me, or I will loose my temper.", "The rage of an elder god unleashed."]

authors = {}
authors["Obi-Wan Kenobi"] = obi_wan_quotes
authors["Ceasar"] = ceasar_quotes
authors["hedge"] = hedge_quotes
authors["mael"] = mael_quotes

for (author, quotes) in authors.items():
    for quote in quotes:
        string_to_output = author + " says, \"" + quote + "\""
        print(string_to_output)
