# Ask user search/add notes function
def choose_feature():
    user_choice = input("What do you want to do?\nEnter '1' to add a note.\nOr '2' to search notes.\nTo stop type 'quit'.\n: ")
    
    if user_choice == "1":
        enter_note()

    elif user_choice == "2":
        search_notes()

    elif user_choice == "quit":
        quit()

    else:
        print("Invalid input.")
        
    return True

# Add note function
def enter_note():
    user_note = input("Enter your note:\n")
    note_file = open("note_file.txt", "a")
    note_file.write(user_note + "\n")
    note_file.close()

def test_file_existance_and_content():
    try:
        note_file = open("note_file.txt")
    except FileNotFoundError as error:
        print("You haven't made any note yet!")
        return True

    if note_file.read() == "":
        print("You haven't made any note yet!")
        note_file.close()
        return True
    else:
        note_file.close()
        return False

# Search note function
def search_notes():
    if test_file_existance_and_content():
        return
    
    user_search = input("Enter your search:\n")
    
    note_file = open("note_file.txt")
    hits = []
    for note in note_file:
        if note.find(user_search) != -1:
            hits.append(note)
    
    if hits:
        for hit in hits:
            print("---------")
            print(hit)
            print()

    else:
        print("---------")
        print("No hit found.")
        print()
    
        
        

# Loop until shutdown
while choose_feature():
    continue