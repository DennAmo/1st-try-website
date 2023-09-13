def create_diary_entry(title, description):
    entry = f"<h1>{title}</h1>\n<h2>{description}</h2>\n\n"
    with open("diary.html", "a") as diary_file:
        diary_file.write(entry)
    print("Diary entry added successfully!")

def display_entries():
    try:
        with open("diary.html", "r") as diary_file:
            entries = diary_file.read()
            print(entries)
    except FileNotFoundError:
        print("Aucune entrée de journal n'a été créée.")

def delete_entry():
    display_entries()  # Affiche d'abord la liste des entrées
    entry_to_delete = input("Enter the entry number to delete: ")
    
    try:
        entry_to_delete = int(entry_to_delete)
        with open("diary.html", "r") as diary_file:
            lines = diary_file.readlines()
        if 1 <= entry_to_delete <= len(lines):
            # Trouver l'index de début et de fin de l'entrée à supprimer
            start_index = (entry_to_delete - 1) * 4  # Chaque entrée a 4 lignes
            end_index = start_index + 3
            
            # Supprimer les lignes correspondant à l'entrée
            del lines[start_index:end_index + 1]
            
            with open("diary.html", "w") as diary_file:
                diary_file.writelines(lines)
            print(f"Diary entry {entry_to_delete} deleted successfully.")
        else:
            print("Entrée invalide. Rien n'a été supprimé.")
    except ValueError:
        print("Entrée invalide. Veuillez saisir un numéro valide.")
    except FileNotFoundError:
        print("Aucune entrée de journal n'a été créée.")

def main():
    print("Simple Diary Application")

    while True:
        print("\nOptions:")
        print("1. Add Diary Entry")
        print("2. Delete Diary Entry")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the entry title: ")
            description = input("Enter the entry description: ")
            create_diary_entry(title, description)
        elif choice == "2":
            delete_entry()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()