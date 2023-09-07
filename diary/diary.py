def create_diary_entry(title, description):
    entry = f"<h1>{title}</h1>\n<h2>{description}</h2>\n\n"
    with open("diary.html", "a") as diary_file:
        diary_file.write(entry)
    print("Diary entry added successfully!")

def main():
    print("Simple Diary Application")

    while True:
        print("\nOptions:")
        print("1. Add Diary Entry")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the entry title: ")
            description = input("Enter the entry description: ")
            create_diary_entry(title, description)
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
