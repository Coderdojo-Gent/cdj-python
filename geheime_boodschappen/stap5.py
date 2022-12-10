## Stap 5: Ontcijfer de boodschap

alfabet = "abcdefghijklmnopqrstuvwxyz"
sleutel = int(input("Welke sleutel zou je graag gebruiken bij de versleuteling? "))

message = input("Welke boodschap zou je graag versleutelen? ")
new_message = ""
for character in message:
    character = character.lower()
    if character in alfabet:
        position = alfabet.find(character)
        new_position = (position - sleutel) % 26
        new_character = alfabet[new_position]
        new_message += new_character
    else:
        new_message += character
print("De versleutelde boodschap is: ", new_message)