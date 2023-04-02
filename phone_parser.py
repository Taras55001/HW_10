from collections import UserDict

contacts_list = {"test": [12345], "test2": [12345,]}
command_list = "'add' - додає новий контакт\n"\
    "'change' - змінює контакт\n"\
    "'delete' - видаляє конакт за ім'ям\n"\
    "'show' - показує список конактів\n"\
    "'good', 'bye', 'close', 'exit' - вихід з бота"
input_line = "-" * 50 + "\n"\
    "Введіть команду \n"\
    "(example: 'add name phone_number')\n"\
    "Щоб відобразии список команд введіть 'help': "


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def delete_record(self, name):
        self.data.pop(name)


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


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Контакт не знайдено")
        except ValueError:
            print("Номер телефону повинен містити тільки цифри")
        except IndexError:
            print("Недостатньо аргументів")
    return wrapper


def add_record(command):
    if spliting_arguments(command):
        record = spliting_arguments(command)
        book.add_record(record)
    else:
        return False


@input_error
def delete(command):
    argument = command.strip().split()[1]
    if argument:
        book.delete_record(argument)
    return argument


@input_error
def parse_command(command):
    key, name, phone = command.strip().split()
    return key, name, phone


def spliting_arguments(command):
    try:
        key, arg1, arg2 = parse_command(command)
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
        elif command.startswith("add") or command.startswith("change"):
            add_record(command)
            if parse_command(command):
                print(
                    f"Контакт {parse_command(command)[1]} з номером {parse_command(command)[2]} збережено")
            elif parse_command(command):
                print(
                    f"Номер телефону для контакту {parse_command(command)[1]} змінено на {parse_command(command)[2]}")
        elif command.startswith("delete"):
            print(f"конакт за ім'ям {delete(command)} видалений")
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
