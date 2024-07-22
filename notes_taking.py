def display_menu():
    print("Menu:")
    print("1. View notes")
    print("2. Add a new note")
    print("3. Search for a note by title")
    print("4. Delete a note")
    print("5. Exit")

def view_notes(notes):
    if not notes:
        print("No notes available.")
    else:
        for title, content in notes.items():
            print(f"Title: {title}")
            print(f"Content: {content}")
            print("-" * 20)

def add_note(notes):
    title = input("Enter the note title: ")
    if title in notes:
        print("A note with this title already exists.")
    else:
        content = input("Enter the note content: ")
        notes[title] = content
        print("Note added.")

def search_note(notes):
    title = input("Enter the note title to search for: ")
    if title in notes:
        print(f"Content: {notes[title]}")
    else:
        print("Note not found.")

def delete_note(notes):
    title = input("Enter the note title to delete: ")
    if title in notes:
        del notes[title]
        print("Note deleted.")
    else:
        print("Note not found.")

def main():
    notes = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_notes(notes)
        elif choice == '2':
            add_note(notes)
        elif choice == '3':
            search_note(notes)
        elif choice == '4':
            delete_note(notes)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()