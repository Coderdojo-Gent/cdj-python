## Stap 2: Meerdere sleutels

alfabet = "abcdefghijklmnopqrstuvwxyz"
sleutel = int(input("Welke sleutel zou je graag gebruiken bij de versleuteling? "))

character = input("Welke letter zou je graag versleutelen? ")
character = character.lower()
position = alfabet.find(character)
new_position = (position + sleutel) % 26
new_character = alfabet[new_position]
print("De versleutelde letter is: ", new_character)