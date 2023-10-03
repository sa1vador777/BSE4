# -*- coding: utf-8 -*-

def main() -> str:
    
    a1 = 5
    a2 = 4
    b = 6
    
    result = (a2 * 10) + a1 + b
    result_a2 = result // 10  
    result_a1 = result % 10 

    return f"Сумма: {a2}{a1} + {b} = {result_a2}{result_a1}"


if __name__ == "__main__":
    print(main())
