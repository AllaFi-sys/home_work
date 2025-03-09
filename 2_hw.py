def task_1() -> None:
    # Создаем 5 переменных с разными типами данных
    integer_var: int = 42
    float_var: float = 3.14
    string_var: str = "Hello, World!"
    list_var: list = [1, 2, 3, 4, 5]
    bool_var: bool = True

    # Выводим типы данных каждой переменной
    print(f"Тип integer_var: {type(integer_var)}")
    print(f"Тип float_var: {type(float_var)}")
    print(f"Тип string_var: {type(string_var)}")
    print(f"Тип list_var: {type(list_var)}")
    print(f"Тип bool_var: {type(bool_var)}")

# Вызов функции
task_1()