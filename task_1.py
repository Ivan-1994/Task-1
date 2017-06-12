#Задание (1).docx
from pprint import PrettyPrinter


def my_decorator1(function_to_decorate):
    def my_wrapper1(my_list):
        i_list = list()
        for i in my_list:
            if ' М ' in i or ' м ' in i:
                i_list.append('Г-н ' + i.replace('М ', ''))
            elif ' Ж ' in i or ' ж ' in i:
                i_list.append('Г-жа ' + i.replace('Ж ', ''))
        i_list = sorted(i_list, key=lambda age: age.split(' ')[3])
        function_to_decorate(i_list)
    return my_wrapper1


@my_decorator1
def my_func(my_list):
    pp = PrettyPrinter().pprint
    pp(my_list)


if __name__ == '__main__':
    my_list = ('Иван Петров М 34', 'Сергей Терехов М 25', 'Александра Кац Ж 23', 'Семен Бурденко М 25')
    #for i in range(int(input())):
    #    my_list.append(input())
    my_func(my_list)
