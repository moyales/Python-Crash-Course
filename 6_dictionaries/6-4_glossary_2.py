#6.4: Glossary 2
#Clean up the code from 6.3 using loops and add five more terms.

python_terms = {
	"string" : "sequence of characters enclosed in quotations",
	"list" : "collection of items in a particular order",
	"tuple" : "list of items that cannot change",
	"dictionary" : "connecting pieces of related information",
	"comment" : "notes within programming indicated by a #",
	"loop" : "repeating an action or set of actions for given data",
	"syntax" : "the way code is written and structured",
	"python" : "the programming language this glossary is written in",
	"slice" : "group of items from a list",
	"boolean expression" : "expression that returns T or F"
	}

for term, definition in sorted(python_terms.items()):
	print(term.title() + ":")
	print(definition + "\n")
