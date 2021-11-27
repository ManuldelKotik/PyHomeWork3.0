def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'Некорректные данные'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'

print(div(input('Введите перое число - '), input('Введите второе число - ')))
