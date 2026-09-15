def add(*args):
    total = 0

    for number in args:
        total += number

    print("Total:", total)

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40, 50)