import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes_needed = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
    "perimeter-triangle": 3,
    "area-triangle": 3
}


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    if fig not in figs:
        return f"Invalid figure: {fig}"  # Вернуть сообщение об ошибке

    if func not in funcs:
        return f"Invalid function: {func}"  # Вернуть сообщение об ошибке


    if any(x <= 0 for x in size):
        return "All elements must be positive!"  # Возвращаем сообщение об ошибке

    if fig == 'triangle':
        a, b, c = size
        if not (a + b > c and a + c > b and b + c > a):
            return "Can not make a triangle out of these elements"  # Возвращаем сообщение об ошибке

    try:
        result = eval(f'{fig}.{func}(*{size})')
        return result  # Возвращаем результат вычислений
    except (NameError, AttributeError, TypeError) as e:
        return f"Error: {e}"  # Возвращаем сообщение об ошибке

if __name__ == "__main__":
    while True:  # Бесконечный цикл, пока пользователь не выберет выход.
        fig = input("Enter figure name (circle, square, triangle, or quit): ").lower()
        if fig == 'quit':
            break

        if fig not in figs:
            print("Invalid figure name.")
            continue

        func = input("Enter function name (perimeter, area): ").lower()
        if func not in funcs:
            print("Invalid function name.")
            continue


        needed_sizes = sizes_needed.get(f"{func}-{fig}")
        if needed_sizes is None:
            print("Invalid combination of figure and function.")
            continue

        while True:
            try:
                sizes_str = input(f"Input figure sizes separated by space ({needed_sizes} for {fig}): ")
                sizes = list(map(float, sizes_str.split()))
                if len(sizes) != needed_sizes:
                    print(f"Incorrect number of sizes. Please enter {needed_sizes} values.")
                    continue
                break  # Выход из цикла, если ввод корректен
            except ValueError:
                print("Invalid input. Please enter numbers separated by spaces.")


        result = calc(fig, func, sizes)

        if isinstance(result, str):  # Обрабатываем ошибки как строки
            print(result)
            break
        else:
            print(result)
            break
