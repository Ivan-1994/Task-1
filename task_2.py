#Задание (1).docx
def my_func(list_x, y):
    i = 0
    for x in list_x:
        if y == x:
            i += 1
    return i


if __name__ == '__main__':
    """
    list_x = list()
    for x in range(int(input())):
        list_x.append(input())

    list_y = list()
    for y in range(int(input())):
        list_y.append(input())
    """
    list_x = ('икс', 'зэт', 'альфа', 'варо', 'икс', 'икс')
    list_y = ('икс', 'зэт', 'вап',)
    for y in list_y:
        print(my_func(list_x, y))