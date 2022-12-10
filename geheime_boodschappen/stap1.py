## Stap 1: Versleutel 1 letter

alfabet = "abcdefghijklmnopqrstuvwxyz"
sleutel = 3

character = input("Welke letter zou je graag versleutelen? ")
character = character.lower()
position = alfabet.find(character)
new_position = (position + sleutel) % 26
new_character = alfabet[new_position]
print("De versleutelde letter is: ", new_character)