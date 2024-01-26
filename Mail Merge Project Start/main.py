PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt")as f:
    names=f.readlines()
    
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_file=letter.read()
    for name in names:
        new_name=name.strip()
        new_letter=letter_file.replace(PLACEHOLDER,new_name)
        with open(f"./Output/ReadyToSend/letter_to_{new_name}.txt","w") as f:
            f.write(new_letter)
            