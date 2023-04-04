from collections import UserDict

command_list = "'add' - додає новий контакт\n"\
    "'change' - змінює контакт\n"\
    "'delete' - видаляє конакт за ім'ям\n"\
    "'show' - показує список конактів\n"\
    "'good', 'bye', 'close', 'exit' - вихід з бота"
input_line = "-" * 50 + "\n"\
    "Введіть команду \n"\
    "(example: 'add name phone_number')\n"\
    "Щоб відобразити список команд введіть 'help': "


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record.phones

    def delete_record(self, name):
        self.data.pop(name)


class Field:
    pass


class Name(Field):
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
        self.phones = []

    def add_phone(self):
        if self.phone not in self.phones:
            self.phones.append(self.phone)
        book.add_record(self)

    def change_phone(self, new_phone):
        if self.phone in self.phones:
            self.phones.remove(self.phone)
            self.phones.append(new_phone)

    def delet_phone(self):
        self.phones.remove(self.phone)


class Phone(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


book = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print("Контакт не знайдено")
        except ValueError:
            print("Номер телефону повинен містити тільки цифри")
        except TypeError:
            print("Недостатньо аргументів")
    return wrapper


def iter_phones(name):
    for n, p in book.data.items():
        if n == name:
            return ', '.join(p.phone.value)


@input_error
def add_record(command):
    if len(parse_command(command)) >= 3:
        name, phone = spliting_arguments(command)
        record = Record(name, phone)
        return record.add_phone()
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
    key, arg1, arg2 = parse_command(command)
    name = Name(arg1)
    phone = Phone(arg2)
    return name, phone


def main():

    while True:

        command = input(input_line).lower()
        if not command:
            print("Невідома команда")
        elif command.startswith("hello"):
            print("How can I help you?")
        elif command.startswith("add") or command.startswith("change"):
            add_record(command)
            if parse_command(command) and command.startswith("add"):
                print(
                    f"Контакт {parse_command(command)[1]} з номером {parse_command(command)[2]} збережено")
            elif parse_command(command) and command.startswith("change"):
                print(
                    f"Номер телефону для контакту {parse_command(command)[1]} змінено на {parse_command(command)[2]}")
        elif command.startswith("delete"):
            print(f"конакт за ім'ям {delete(command)} видалений")
        elif command.startswith("show"):
            print('\n'.join([f'{name}: {", ".join(phone.value for phone in phones)}'
                             for name, phones in book.data.items()]))
        elif command.startswith("help"):
            print(command_list)

        elif command.split()[0] in ["good", "bye", "close", "exit"]:
            print("Good bye!")
            break


if __name__ == '__main__':
    main()
