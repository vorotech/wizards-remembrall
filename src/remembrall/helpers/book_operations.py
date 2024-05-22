from .wrappers import input_error
from classes import AddressBook, Record

@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        err = record.add_phone(phone)
        if err:
            if message == "Contact added.":
                print(err)
                message = "Contact added without phone"
            else:
                message = err
    return message

@input_error
def change_contact(args: list, book: AddressBook) -> str:
    name, new_name = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    book.change_name(name, new_name)
    return "Contact updated."

@input_error
def remove_contact(args: list, book: AddressBook) -> str:
    name = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    book.remove_record(name)
    return "Contact removed."

@input_error
def change_phone(args: list, book: AddressBook) -> str:
    name, phone, new_phone = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.edit_phone(phone, new_phone)
    return "Contact updated."

@input_error
def remove_phone(args: list, book: AddressBook) -> str:
    name, phone = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.remove_phone(phone)
    return "Contact updated."

@input_error
def get_contact_phones(args: list, book: AddressBook) -> str:
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    if not found.phones:
        return "Contact has no phone numbers."
    return f"{'; '.join(p.value for p in found.phones if p.value)}"

@input_error
def get_all_contacts(book: AddressBook) -> str:
    if not len(book):
        return "Address book is empty"
    output = "Address book:"
    for record in book.data.values():
        output += f"\n{record}"
    return output

@input_error
def add_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.add_birthday(birthday)
    return "Birthday added"

@input_error
def show_birthday(args: list, book: AddressBook) -> str:
    name = args[0]
    found = book.find(name)
    if not found:
        return "Contact not found."
    if not found.birthday:
        return "Contact has no birthday date."
    return found.birthday

@input_error
def change_birthday(args: list, book: AddressBook) -> str:
    name, birthday = args
    found = book.find(name)
    if not found:
        return "Contact not found."
    found.edit_birthday(birthday)
    return "Birthday changed"

@input_error
def get_birthdays(args: list, book: AddressBook) -> str:
    days = int(args[0])
    if not len(book):
        return "Address book is empty"
    birthdays = book.get_upcoming_birthdays(days)
    if not birthdays:
        return "No upcoming birthdays"
    output = "Upcoming birthdays:"
    for record in birthdays:
        output += f"\n{record}"
    return output