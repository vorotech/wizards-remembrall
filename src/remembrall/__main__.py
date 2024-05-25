"""Assistant bot for wizards of the academy.

Usage:
--------

    $ remembrall [command] [args1, args2, ...]

List the avaialble commands:

    $ remembrall help

Version:
--------

- wizards-remembrall v1.0.0
"""

import sys
from remembrall.classes import Record
from remembrall.helpers import book_operations
from remembrall.helpers.data_upload import load_data, save_data, load_notebook_data, save_notebook_data
from remembrall.helpers.greeting import farewell, greeting
from remembrall.helpers.help_function import show_help
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from remembrall.helpers.intellectual_analysis import session

def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main(test_users = None):
    book = load_data()
    load_test = len(sys.argv)>1 and sys.argv[1] =="test" and test_users and not book.data
    if load_test:
        for user in test_users:
            rec = Record(user['name'])
            if user['phone']:
                rec.add_phone(user['phone'])
            if user['birthday']:
                rec.add_birthday(user['birthday'])
            if user['address']:
                rec.add_address(user['address'])
            book.add_record(rec)
        print("Test data added")
    greeting()
    while True:
        user_input = session.prompt("Enter a command: ", auto_suggest=AutoSuggestFromHistory(), complete_while_typing=False)
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                save_data(book)
                farewell()
                break
            case "hello":
                print("How can I help you?")
            case "all-contacts":
                # show contacts with all info about them
                print(book_operations.get_all_contacts(book))
            case "add-contact":
                # add contact by name with phone
                print(book_operations.add_contact(args, book))
            case "show-contact":
                # show contact with all info
                print(book_operations.show_contact(args, book))
            case "change-contact":
                # change contact name
                print(book_operations.change_contact(args, book))
            case "remove-contact":
                # remove contact
                print(book_operations.remove_contact(args, book))
            case "change-phone":
                # change contact phone
                print(book_operations.change_phone(args, book))
            case "remove-phone":
                # remove contact phone
                print(book_operations.remove_phone(args, book))
            case "add-birthday":
                # add contact birthday
                print(book_operations.add_birthday(args, book))
            case "change-birthday":
                # change contact birthday
                print(book_operations.change_birthday(args, book))
            case "birthdays":
                # get upcoming birthdays
                print(book_operations.get_birthdays(args, book))
            case "add-email":
                # add contact email
                print(book_operations.add_email(args, book))
            case "change-email":
                # change contact email
                print(book_operations.change_email(args, book))
            case "remove-email":
                # change contact email
                print(book_operations.remove_email(args, book))                
            case "add-address":
                # add contact address
                print(book_operations.add_address(args, book))
            case "change-address":
                # change contact address
                print(book_operations.change_address(args, book))
            case "remove-address":
                # remove contact address
                print(book_operations.remove_address(args, book))
            case "all-notes":
                # show all notes
                print(book_operations.get_all_notes(notebook))
            case "add-note":
                # add note with title and text
                print(book_operations.add_note(args, notebook))
            case "show-note":
                # show note with all info
                print(book_operations.show_note(args, notebook))
            case "change-note":
                # change note text
                print(book_operations.change_note(args, notebook))
            case "remove-note":
                # remove note
                print(book_operations.remove_note(args, notebook))
            case "change-title":
                # change note title
                print(book_operations.change_note_title(args, notebook))
            case "add-tag":
                # add note tag
                print(book_operations.add_note_tag(args, notebook))
            case "remove-tag":
                # remove note tag
                print(book_operations.remove_note_tag(args, notebook))
            case "sort-tags":
                # sort notes by tags
                print(book_operations.sort_notes_by_tags(args, notebook))
            case "find-content":
                # find notes by content
                print(book_operations.find_notes_with_content(args, notebook))
            case "help":
                show_help()
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    users = [
        {"name": "Doe", "phone": "", "birthday": "21.01.1985", "address": "123 Maple St"},
        {"name": "John", "phone": "0987654321", "birthday": "", "address": "456 Elm St"},
        {"name": "John Doe", "phone": "7894561230", "birthday": "23.01.1985", "address": "789 Oak St"},
        {"name": "Jane Smith", "phone": "1234567890", "birthday": "27.01.1990", "address": "987 Pine St"},
        {"name": "Jane", "phone": "3216549870", "birthday": "28.01.1990", "address": "654 Birch St"},
        {"name": "Smith", "phone": "0321654987", "birthday": "29.01.1990", "address": "321 Cedar St"}
    ]
    main(users)
