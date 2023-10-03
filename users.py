# -*- coding: utf-8 -*-

def main() -> str:
    name = input("Whats your name?: ")
    age = input("How old are you?: ")
    area = input("Where are you live?: ")
    
    return f"This is {name}\nIt is {age}\n(s)he live in {area}"


if __name__ == "__main__":
    print(main())
