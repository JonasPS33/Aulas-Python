def somar():
    print("Soma valorews")


def multi():

    print("Valores multiplicados")


def find_index(to_find, item):

    for i , valor in enumerate(to_find):
        if valor == item:
            return i
    return -1
