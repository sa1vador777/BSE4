# -*- coding: utf-8 -*-
import math


def main() -> str:
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите первое число: "))
        
        abs1 = abs(num1)
        abs2 = abs(num2)
        mean_arithmetic = (abs1 + abs2) / 2
        mean_geometric = math.sqrt(abs1 * abs2)
        return f"Среднее арифметическое: {mean_arithmetic}\nСреднее геометрическое: {mean_geometric}"
    except:
        return "Введите число"


if __name__ == "__main__":
    print(main())
    