# -*- coding: utf-8 -*-

def main() -> str:
    
    nums_input = input("Введите четыре числа через пробел: ")
    nums_list: list = nums_input.split(' ')
    if len(nums_list) == 4:
        try:
            for num in nums_list:
                int(num)
            first_sum = int(nums_list[0]) + int(nums_list[1])
            second_sum = int(nums_list[2]) + int(nums_list[3])
            result = round(first_sum/second_sum, 2)
            return f"{result}"
        except:
            return "Введите числа"
    
    else:
        return "Введите четыре числа. Например: X Y Z F"
            

if __name__ == "__main__":
    print(main())
    