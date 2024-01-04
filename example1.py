def get_color(row, col):

    if row % 2 == col % 2:
        return "WHITE"
    return "BLACK"


print(get_color(0,0))
print(get_color(0,1))
print(get_color(2,1))
print(get_color(2,2))
print(get_color(7,7))
print(get_color(-7,7))
print(get_color(8,9))
