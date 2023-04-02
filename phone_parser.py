from collections import UserDict

contacts_list = {"test": [12345], "test2": [12345,]}
command_list = "'add' - додає новий контакт\n"\
    "'change' - змінює контакт\n"\
    "'phone' - показує конакт за ім'ям\n"\
    "'show' - показує список конактів\n"\
    "'good', 'bye', 'close', 'exit' - вихід з бота"
input_line = "-" * 50 + "\n"\
    "Введіть команду \n"\
    "(example: 'add name phone_number')\n"\
    "Щоб відобразии список команд введіть 'help': "


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Name:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Phone(Name):
    pass


class Record(UserDict):
    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone


class Field:
    pass


class Phone(Name):
    def __init__(self, value):
        super().__init__(value)
        self.phones_list = []


book = AddressBook()


def add_record(command):
    record = spliting_arguments(command)
    book.add_record(record)


def change_phone(command):
    atribute = spliting_arguments(command)
    book.change_record(atribute)


def parse_command(command):
    name, phone = command.strip().split()[1], command.strip().split()[2]
    return name, phone


def spliting_arguments(command):
    arg1, arg2 = parse_command(command)
    name = Name(arg1)
    phone = Phone(arg2)
    return Record(name, phone)


def main():

    while True:

        command = input(input_line)
        if command.startswith("add"):
            add_record(command)
        elif command.startswith("change"):
            pass
        elif command.split()[0] == 'show':
            for n in book.data:
                print(str(n), book.data[n].phone)

            pass
        elif command.split()[0] in ['good', 'bye', 'close', 'exit']:
            print("Good bye!")
            break


if __name__ == '__main__':
    main()
