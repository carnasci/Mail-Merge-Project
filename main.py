#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    s_letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = s_letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as new_letter_file:
            new_letter_file.write(new_letter)






