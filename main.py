import json 

DATA_FILE = "people.json"

def load_people():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_people(people):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(people, file, ensure_ascii=False, indent=2)

def list_people(people):
    if not people:
        print("No people found.")
        return

    for index, person in enumerate(people, start=1):
        print(f"{index}. Name: {person['name']}, Age: {person['age']}")

def add_person(people):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    people.append({
        "name": name,
        "age": age
    })

    save_people(people)
    print("Person added successfully.")

def update_person_age(people):
    name = input("Enter the name to update: ")

    for person in people:
        if person["name"].lower() == name.lower():
            new_age = int(input("Enter new age: "))
            person["age"] = new_age
            save_people(people)
            print("Age updated successfully.")
            return

    print("Person not found.")

def search_person(people):
    name = input("Enter name to search: ")

    for person in people:
        if person["name"].lower() == name.lower():
            print(f"Name: {person['name']}, Age: {person['age']}")
            return

    print("Person not found.")

def main():
    people = load_people()

    while True:
        print("\n--- Person Management System ---")
        print("1. List people")
        print("2. Add person")
        print("3. Update person age")
        print("4. Search person")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_people(people)
        elif choice == "2":
            add_person(people)
        elif choice == "3":
            update_person_age(people)
        elif choice == "4":
            search_person(people)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
	main()                                                                                                                                                                                                  

