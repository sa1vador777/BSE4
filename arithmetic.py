# -*- coding: utf-8 -*-

def main() -> str:
    
    try:
        solution = int(input("Решите пример: 4*100-54: "))
        if solution == 344:
            return "Ответ верный"
        else:
            return "Ответ неверный, верный: 344"
    except:
        return "Введите число"


if __name__ == "__main__":
    print(main())
    