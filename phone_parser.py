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

    def change_record(self, record):
        self.data.get()


class Name:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Record:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone


class Field:
    pass


class Phone(Name):
    def __init__(self, value):
        super().__init__(value)


book = AddressBook()


def add_record(command):
    if spliting_arguments(command):
        record = spliting_arguments(command)
        book.add_record(record)
    else:
        return False


def parse_command(command):
    try:
        name = command.strip().split()[1]
        phone = command.strip().split()[2]
        return name, phone
    except IndexError:
        print("Не вказані дані контакту")


def spliting_arguments(command):
    try:
        arg1, arg2 = parse_command(command)
        name = Name(arg1)
        phone = Phone(arg2)
        return Record(name, phone)
    except TypeError:
        return False


def main():

    while True:

        command = input(input_line).lower()
        if not command:
            print("Невідома команда")
        elif command.startswith("hello"):
            return print("How can I help you?")
        elif spliting_arguments(command) and command.startswith("add") or command.startswith("change"):
            add_record(command)
            if command.startswith("add"):
                print(
                    f"Контакт {parse_command(command)[0]} з номером {parse_command(command)[1]} збережено")
            else:
                print(
                    f"Номер телефону для контакту {parse_command(command)[0]} змінено на {parse_command(command)[1]}")
        elif command.startswith("show"):
            for n in book.data:
                print(str(n), book.data[n].phone)
        elif command.startswith("help"):
            print(command_list)

        elif command.split()[0] in ["good", "bye", "close", "exit"]:
            print("Good bye!")
            break


if __name__ == '__main__':
    main()
