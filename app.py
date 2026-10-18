import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


def display_users(users):
    print("\n" + "=" * 70)
    print("USER LIST")
    print("=" * 70)

    for user in users:
        print(
            f"ID: {user['id']} | "
            f"Name: {user['name']} | "
            f"Email: {user['email']} | "
            f"City: {user['address']['city']}"
        )


def search_users(users, keyword):
    keyword = keyword.lower()

    results = []

    for user in users:
        if (
            keyword in user["name"].lower()
            or keyword in user["email"].lower()
            or keyword in user["address"]["city"].lower()
        ):
            results.append(user)

    return results


def main():
    print("Fetching data from API...")

    try:
        users = fetch_users()
        print("Data fetched successfully!")

    except requests.exceptions.RequestException as error:
        print("Error:", error)
        return

    while True:
        print("\nMenu")
        print("1. Display all users")
        print("2. Search users")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_users(users)

        elif choice == "2":
            keyword = input("Enter name, email, or city to search: ")

            results = search_users(users, keyword)

            if results:
                display_users(results)
            else:
                print("\nNo matching users found.")

        elif choice == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()