## Stap 3: Boodschappen versleutelen

alfabet = "abcdefghijklmnopqrstuvwxyz"
sleutel = int(input("Welke sleutel zou je graag gebruiken bij de versleuteling? "))

message = input("Welke boodschap zou je graag versleutelen? ")
new_message = ""
for character in message:
    character = character.lower()
    position = alfabet.find(character)
    new_position = (position + sleutel) % 26
    new_character = alfabet[new_position]
    new_message += new_character
print("De versleutelde boodschap is: ", new_message)