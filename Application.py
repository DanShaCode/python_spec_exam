import os
from datetime import datetime
import csv

notes = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("============================")
    print("       -= NOTEBOOK =-")
    print("============================")
    print()
    print("           MENU")
    print()
    print("     1. Show all notes")
    print("     2. Add note")
    print("     3. Read note")
    print("     4. Edit note")
    print("     5. Delete")
    print("     6. Save to CSV")
    print("     7. Read from CSV")
    print("     8. Exit")
    print()

def show_all_notes():
    clear_screen()
    if len(notes) == 0:
        print("No notes found.")
    else:
        print("========= ALL NOTES =========")
        print()
        filter_date = input("Enter filter date (YYYY-MM-DD) (leave blank for all notes): ")
        print()
        notes_found = False
        for note in notes:
            if filter_date == "" or note['timestamp'].startswith(filter_date):
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Body: {note['body']}")
                print(f"Created/Last Modified: {note['timestamp']}")
                print()
                notes_found = True
        if not notes_found:
            print(f"No notes found for the date: {filter_date}")
        print("========= END OF NOTES =========")
    wait_for_user()

def add_note():
    clear_screen()
    print("========= ADD NOTE =========")
    print()
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if len(notes) > 0:
        new_id = notes[-1]['id'] + 1
    else:
        new_id = 1
    
    note = {
        'id': new_id,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    print("Note added successfully!")
    wait_for_user()

def read_note():
    clear_screen()
    if len(notes) == 0:
        print("No notes found.")
        wait_for_user()
    else:
        print("========= READ NOTE =========")
        print()
        note_id = input("Enter note ID: ")
        for note in notes:
            if str(note['id']) == note_id:
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Body: {note['body']}")
                print(f"Created/Last Modified: {note['timestamp']}")
                break
        else:
            print("Note not found.")
        wait_for_user()

def edit_note():
    clear_screen()
    if len(notes) == 0:
        print("No notes found.")
        wait_for_user()
    else:
        print("========= EDIT NOTE =========")
        print()
        note_id = input("Enter note ID: ")
        for note in notes:
            if str(note['id']) == note_id:
                print(f"ID: {note['id']}")
                print(f"Title: {note['title']}")
                print(f"Body: {note['body']}")
                print()
                new_title = input("Enter new title (leave blank to keep the same): ")
                new_body = input("Enter new body (leave blank to keep the same): ")
                if new_title != "":
                    note['title'] = new_title
                if new_body != "":
                    note['body'] = new_body
                note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("Note edited successfully!")
                break
        else:
            print("Note not found.")
        wait_for_user()

def delete_note():
    clear_screen()
    if len(notes) == 0:
        print("No notes found.")
        wait_for_user()
    else:
        print("========= DELETE NOTE =========")
        print()
        print("Choose an option:")
        print("1. Delete a specific note by ID")
        print("2. Delete all notes")
        print("3. Cancel")
        print()
        delete_option = input("Enter number from menu: ")
        if delete_option == "1":
            note_id = input("Enter note ID: ")
            for note in notes:
                if str(note['id']) == note_id:
                    notes.remove(note)
                    print("Note deleted successfully!")
                    break
            else:
                print("Note not found.")
        elif delete_option == "2":
            confirm = input("Are you sure you want to delete all notes? (Y/N): ")
            if confirm.upper() == "Y":
                notes.clear()
                print("All notes deleted successfully!")
            else:
                print("Delete canceled.")
        elif delete_option == "3":
            print("Delete canceled.")
        else:
            print("Invalid option. Please try again.")
        wait_for_user()

def save_to_csv():
    clear_screen()
    if len(notes) == 0:
        print("No notes found to save.")
        wait_for_user()
    else:
        csv_filename = input("Enter CSV filename: ")
        if not csv_filename.endswith('.csv'):
            csv_filename += '.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body', 'timestamp']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            for note in notes:
                writer.writerow(note)
        print(f"Notes saved to {csv_filename} successfully!")
        wait_for_user()

def read_from_csv():
    clear_screen()
    csv_filename = input("Enter CSV filename: ")
    if not csv_filename.endswith('.csv'):
        csv_filename += '.csv'
    if not os.path.exists(csv_filename):
        print(f"{csv_filename} does not exist.")
        wait_for_user()
    else:
        with open(csv_filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            notes.clear()
            for row in reader:
                notes.append(row)
        print(f"Notes loaded from {csv_filename} successfully!")
        wait_for_user()

def wait_for_user():
    input("Press Enter to continue...")
    clear_screen()
    show_menu()
    choice = input("Enter menu number: ")
    process_choice(choice)

def process_choice(choice):
    if choice == "1":
        show_all_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        read_note()
    elif choice == "4":
        edit_note()
    elif choice == "5":
        delete_note()
    elif choice == "6":
        save_to_csv()
    elif choice == "7":
        read_from_csv()
    elif choice == "8":
        clear_screen()
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        wait_for_user()

clear_screen()
show_menu()
choice = input("Enter menu number: ")
process_choice(choice)