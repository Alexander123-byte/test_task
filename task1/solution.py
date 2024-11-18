def strict(func):
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов функции
        annotations = func.__annotations__

        # Проверяем соответствие типов
        for arg_name, arg_value in zip(annotations.keys(), args):
            expected_type = annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(
                    f'Аргумент "{arg_name}" должен быть {expected_type.__name__}, получен {type(arg_value).__name__}')

        # Вызываем оригинальную функцию
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# Примеры использования
# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError
