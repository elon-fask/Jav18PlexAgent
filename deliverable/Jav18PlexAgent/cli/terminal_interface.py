# Provides an interactive terminal interface for user interaction
def start_terminal():
    print("Welcome to the Plex Agent Terminal")
    print("Commands:")
    print("1. View logs")
    print("2. Check database status")
    print("3. Exit")

    while True:
        command = input("Enter command: ")
        if command == "1":
            print("Displaying logs...")  # Placeholder for log display
        elif command == "2":
            print("Database status: OK")  # Placeholder for database status
        elif command == "3":
            print("Exiting terminal.")
            break
        else:
            print("Invalid command. Please try again.")
