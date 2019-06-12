# Ask user for note file to use
def define_notefile():
    user_file_input = input("Enter note file to use: ").strip()
    print()
    return user_file_input

# Ask user search/add notes function
def choose_feature(file):
    user_choice = input("What do you want to do?\nType '1' to add a note.\nType '2' to search notes.\nType '3' to quit the program.\n: ").strip()
    
    if user_choice == "1":
        enter_note(file)

    elif user_choice == "2":
        hits = search_notes(file)

        if hits:
            ask_to_remove_note(hits, file)

    elif user_choice == "quit":
        print("\nApplication terminated.\nBye!\n")
        quit()

    else:
        print("\nInvalid input.\n")
        
    return True

# Add note function
def enter_note(file):
    user_note = input("Enter your note:\n").strip()
    note_file = open(file, "a")
    note_file.write(user_note + "\n")
    note_file.close()

    print("\nNote written in '" + file + "'.\n")

# Test if the file exist and if it is empty
def test_file_existance_and_content(file):
    try:
        note_file = open(file)
    except FileNotFoundError as error:
        print("\nYou haven't made any note yet!\n")
        return True

    if note_file.read() == "":
        print("\nYou haven't made any note yet!\n")
        note_file.close()
        return True
    else:
        note_file.close()
        return False

# Search note function
def search_notes(file):
    if test_file_existance_and_content(file):
        return False
    
    user_search = input("Enter your search:\n")
    
    note_file = open(file)
    hits = []
    for note in note_file:
        if note.find(user_search) != -1:
            hits.append(note)
    
    if hits:
        counter = 0
        for hit in hits:
            counter += 1
            print("---------")
            print("Hit " + str(counter)  + ":\n")
            print(hit)
            print()

    else:
        print("---------")
        print("No hit found.")
        print()

    note_file.close()

    return hits

# Remove note function
def ask_to_remove_note(hits, file):
    user_answer =  input("Do you want to remove a note? ").strip().upper()

    if user_answer == "YES" or user_answer == "Y":
        user_hits_to_remove = input("Enter space saparated list of hit's number to be removed:\n").strip().split(" ")
        hits_to_remove =[]

        for number in user_hits_to_remove:
            index = int(number) - 1
            hits_to_remove.append(hits[index])
            
        remove_notes(hits_to_remove, file) 

    elif user_answer == "NO" or user_answer == "N":
        print()
        return

    else:
        print("I will suppose that this means no...\n")
        return

def remove_notes(hits_to_remove, file):
    original_note_file = open(file)
    content = original_note_file.read()
    original_note_file.close()

    for note in hits_to_remove:
        content = content.replace(note, "")
    
    new_note_file = open(file, "w")
    new_note_file.write(content)
    new_note_file.close()

    if len(hits_to_remove) == 1:
        message = " note was removed."
    else:
        message = " notes were removed."

    print()
    print(str(len(hits_to_remove)) + message)
    print()

#Program begin
print("\nNote App started.\n")

note_file = define_notefile()

# Loop until shutdown
while choose_feature(note_file):
    continue