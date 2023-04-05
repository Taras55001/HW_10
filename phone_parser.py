from collections import UserDict


input_line = "-" * 50 + "\n"\
    "Input command \n"\
    "(example: 'add name phone_number')"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record.phones
        return f'Contact {record.name.value} create successful'

    def add_phone(self, name, phone):
        for p in self.data.get(name):
            if phone.value != p.value:
                self.data[name].append(phone)
                return f'Phone {phone} added to contact {name} numbers'
            return f'Contact {name} whith phone {phone} are alredy exist'

    def change_phone(self, name, phone, new_phone):
        for p in self.data.get(name):
            if phone.value == p.value:
                self.data[name].remove(p)
        self.data[name].append(new_phone)

    def delete_record(self, name):
        self.data.pop(name)
        return f'Contact {name} deleted successful'


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
        self.phones = [phone] if phone else []

    def add_phone(self, phone):
        self.phones.append(self.phone)

    def change_phone(self, old_phone, new_phone):
        for p in book.data[self.name.value]:
            if p.value == old_phone.value:
                book.change_phone(self.name.value, old_phone, new_phone)
                return f'Phone {old_phone} change to {new_phone}'
        return f'No phone {old_phone}'

    def delet_phone(self, phone):
        self.phones.remove(phone)


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


def iter_book(command):
    content = '\n'.join(
        [f'{name}: {", ".join(phone.value for phone in phones)}'for name, phones in book.data.items()])
    return content


@input_error
def add_record(command):
    spliting_arguments = command.strip().split()
    if len(spliting_arguments) == 3:
        key, name, phone = spliting_arguments
        rec = book.get(name)
        if rec:
            rec = book.add_phone(name, Phone(phone))
            return rec
        rec = Record(Name(name), Phone(phone))
        result = book.add_record(rec)
        return result


@input_error
def change_record(command):
    arguments = command.strip().split()
    if len(arguments) == 4:
        key, name, phone, new_phone = arguments
        record = Record(Name(name))
        return record.change_phone(Phone(phone), Phone(new_phone))


@input_error
def delete(command):
    argument = command.strip().split()[1]
    if argument:
        return book.delete_record(argument)


def get_func(command):
    arg_list = command.strip().split()
    for key in command_dict.keys():
        if arg_list[0].lower() == 'hello':
            return command_dict[key]
        elif arg_list[0].lower() == key:
            func = command_dict.get(key)
            return func(command)
        elif arg_list[0].lower() in key:
            return command_dict[key]
    raise KeyError("This command doesn't exist")


command_dict = {"hello": "How can I help you?", "add": add_record, "change": change_record, "delete": delete,
                "show": iter_book, ("good", "bye", "close", "exit"): "Good bye!"}


def main():

    while True:

        command = input(input_line).lower()
        try:
            func = get_func(command)
        except KeyError as eror:
            print(eror)
            continue
        print(func)
        if command.split()[0] in ["good", "bye", "close", "exit"]:
            break


if __name__ == '__main__':
    main()
