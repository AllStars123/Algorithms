# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

for num in range(2, 10):
    main_list = [item for item in range(2, 99) if item % num == 0]
    if len(main_list) > 20:
        print(f"Кратны {num} - {len(main_list)} числа")
    else:
        print(f"Кратны {num} - {len(main_list)} чисел")
