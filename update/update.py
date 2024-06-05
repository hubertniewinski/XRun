from typing import Iterable

from models.User import User
from user.initialize import saveUserDecorator


def getValidKeysToUpdate(obj):
    return [key for key, value in obj.__dict__.items() if
            not isinstance(value, Iterable) or isinstance(value, str)]


def update(user: User):
    while True:
        user_dict_keys = getValidKeysToUpdate(user)
        for key in user_dict_keys:
            print(key)

        key_input = input("Enter key to change or 'quit' to quit")

        if key_input == 'quit':
            break

        if key_input not in user_dict_keys:
            print("Invalid key")
            continue

        attr = getattr(user, key_input)

        if isinstance(attr, (int, float, str)):
            print(f"{key_input}: {attr}")
            new_val = input(f"Enter new value of '{key_input}': ")
            setattr(user, key_input, new_val)
            saveUserDecorator(user)
            print(f"Changed value of '{key_input}' to '{new_val}'")
        else:
            while True:
                nested_dict_keys = getValidKeysToUpdate(attr)

                for nested_key in nested_dict_keys:
                    print(nested_key)
                nested_key_input = input("Enter key to change or 'up' to move up in hierarchy")

                if nested_key_input == 'up':
                    break

                if nested_key_input not in nested_dict_keys:
                    print("Invalid key")

                parent = attr
                attr = getattr(attr, nested_key_input)

                if isinstance(attr, (int, float, str)):
                    print(f"{nested_key_input}: {attr}")
                    new_val = input(f"Enter new value of '{nested_key_input}': ")
                    setattr(parent, nested_key_input, new_val)
                    saveUserDecorator(user)
                    print(f"Changed value of '{nested_key_input}' to '{new_val}'")
                    attr = parent
                elif attr.__class__.__name__ == 'HistoryProperty':
                    i = input(f"Enter new value of '{nested_key_input}'")
                    attr.addValue(i)
                    saveUserDecorator(user)
                    print(f"Added value '{i}' to '{nested_key_input}'")
                    attr = parent
