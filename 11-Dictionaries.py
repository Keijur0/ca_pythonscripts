phonebook = {
	"John" : 938477566,
	"Jack" : 938377264,
	"Jill" : 947662781
}

phonebook["Jake"] = 938273443
phonebook.pop("Jill")

if "Jake" in phonebook:
	print("Jake is listing in the phonebook")
if "Jill" not in phonebook:
	print("Jill is not listed in the phonebook")

