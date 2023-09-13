import json

def load_entries():
    try:
        with open("diary.json", "r") as diary_file:
            entries = json.load(diary_file)
    except FileNotFoundError:
        entries = []
    return entries

def save_entries(entries):
    with open("diary.json", "w") as diary_file:
        json.dump(entries, diary_file, indent=4)

def create_diary_entry(entries, title, description):
    entry = {"title": title, "description": description}
    entries.append(entry)
    save_entries(entries)
    print("Diary entry added successfully!")

def display_entries(entries):
    if not entries:
        print("Aucune entrée de journal n'a été créée.")
        return

    print("Index des entrées existantes :")
    for i, entry in enumerate(entries):
        print(f"{i + 1}: {entry['title']} - {entry['description']}")

def delete_entry(entries, entry_to_delete):
    try:
        entry_to_delete = int(entry_to_delete)
        if 1 <= entry_to_delete <= len(entries):
            deleted_entry = entries.pop(entry_to_delete - 1)
            save_entries(entries)
            print(f"Diary entry {entry_to_delete} deleted successfully:\n{deleted_entry['title']} - {deleted_entry['description']}")
        else:
            print("Entrée invalide. Rien n'a été supprimé.")
    except ValueError:
        print("Entrée invalide. Veuillez saisir un numéro valide.")

def main():
    entries = load_entries()

    print("Simple Diary Application")

    while True:
        print("\nOptions:")
        print("1. Add Diary Entry")
        print("2. Display Diary Entries")
        print("3. Delete Diary Entry")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the entry title: ")
            description = input("Enter the entry description: ")
            create_diary_entry(entries, title, description)
        elif choice == "2":
            display_entries(entries)
        elif choice == "3":
            entry_to_delete = input("Enter the entry number to delete: ")
            delete_entry(entries, entry_to_delete)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
