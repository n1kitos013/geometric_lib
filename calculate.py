import circle
import square
import triangle

figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {}


def isTriangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


def calc(fig, func, size):
    assert fig in figs
    assert func in funcs
    if any(x <= 0 for x in size):
        print(f"{fig} for that input doesn`t exist")
        return 404

    if fig == "triangle":
        if not (isTriangle(size[0], size[1], size[2])):
            print("this triangle doesn`t exist")
            return 404
    result = eval(f"{fig}.{func}(*{size})")
    print(f"{func} of {fig} is {result}")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    if fig == "triangle":
        while len(size) != sizes.get(f"{func}-{fig}", 3):
            try:
                size = list(
                    map(
                        float,
                        input("Input figure sizes separated by space\n").split(" "),
                    )
                )
            except Exception:
                print("Incorrect input")
    else:
        while len(size) != sizes.get(f"{func}-{fig}", 1):
            try:
                size = list(
                    map(
                        float,
                        input(
                            "Input figure sizes separated by space, for square and circle 1 num\n"
                        ).split(" "),
                    )
                )
            except Exception:
                print("Incorrect input")

    calc(fig, func, size)
