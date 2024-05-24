

# Методы для работы со строками
str.capitalize()                   # Возвращает строку, в которой первое слово начинается с заглавной буквы
str.casefold()                     # Преобразует строку в нижний регистр, сохраняя алфавитный порядок
str.center(width[, fillchar])      # Возвращает строку, где строка центрирована с помощью заполнителя
str.count(sub[, start[, end]])     # Возвращает количество вхождений подстроки sub в строку
str.encode(encoding=None, errors=None) # Кодирует строку согласно кодировке encoding
str.endswith(suffix[, start[, end]]) # Проверяет, заканчивается ли строка на суффикс
str.expandtabs([tabsize])          # Расширяет tabs до длины tabsize пробелов
str.find(sub[, start[, end]])      # Находит первое вхождение подстроки sub в строке
str.format(*args, **kwargs)        # Форматирует строку согласно позициям или именованным параметрам
str.format_map(mapping)            # То же самое, что str.format(), но принимает словарь mapping
str.index(sub[, start[, end]])     # То же самое, что find(), но с исключением ValueError при пропуске
str.isalnum()                      # Проверяет, состоит ли строка только из буквенно-цифровых символов
str.isalpha()                      # Проверяет, состоит ли строка только из буквенных символов
str.isdecimal()                    # Проверяет, состоит ли строка только из десятичных цифр
str.isdigit()                      # Проверяет, состоит ли строка только из цифровых символов
str.isidentifier()                 # Проверяет, является ли строка допустимым идентификатором
str.islower()                      # Проверяет, состоит ли строка только из строчных букв
str.isnumeric()                    # Проверяет, состоит ли строка только из числовых символов
str.isprintable()                  # Проверяет, состоит ли строка только из печатных символов
str.isspace()                      # Проверяет, состоит ли строка только из пробельных символов
str.istitle()                      # Проверяет, состоит ли строка только из титульных букв
str.isupper()                      # Проверяет, состоит ли строка только из заглавных букв
str.join(iterable)                 # Возвращает новую строку, где элементы iterable разделены данной строкой
str.ljust(width[, fillchar])       # Возвращает строку, где строка дополнена слева до ширины width
str.lower()                        # Преобразует строку в нижний регистр
str.lstrip([chars])                # Удаляет префикс из пробельных или указанных символов
str.maketrans(x[, y[, z]])         # Возвращает объект для транслитерации строк
str.partition(sep)                 # Разделяет строку на три части: до первого вхождения sep, сам sep и после sep
str.replace(old, new[, count])     # Заменяет все вхождения подстроки old на new
str.rfind(sub[, start[, end]])     # Находит последнее вхождение подстроки sub в строке
str.rindex(sub[, start[, end]])    # То же самое, что rfind(), но с исключением ValueError при пропуске
str.rjust(width[, fillchar])       # Возвращает строку, где строка дополнена справа до ширины width
str.rpartition(sep)                # Разделяет строку на три части: до последнего вхождения sep, сам sep и после sep
str.rsplit([sep[, maxsplit]])      # Разделяет строку на список строк по разделителю sep
str.rstrip([chars])                # Удаляет суффикс из пробельных или указанных символов
str.split([sep[, maxsplit]])       # Разделяет строку на список строк по разделителю sep
str.splitlines([keepends])         # Разделяет строку на список строк по переводам строк
str.startswith(prefix[, start[, end]]) # Проверяет, начинается ли строка с префикса





# примеры


# Метод capitalize()
# Возвращает строку, в которой первое слово начинается с заглавной буквы.
example = "hello world"
print(example.capitalize())  # Вывод: "Hello world"

# Метод casefold()
# Преобразует строку в нижний регистр, сохраняя алфавитный порядок.
example = "HelloWorld"
print(example.casefold())  # Вывод: "helloworld"

# Метод center(width[, fillchar])
# Возвращает строку, где строка центрирована с помощью заполнителя.
example = "Hello"
print(example.center(10, "*"))  # Вывод: "****Hello****"

# Метод count(sub[, start[, end]])
# Возвращает количество вхождений подстроки sub в строку.
example = "HelloWorld"
print(example.count("o"))  # Вывод: 2

# Метод encode(encoding=None, errors=None)
# Кодирует строку согласно кодировке encoding.
example = "Привет мир"
print(example.encode("utf-8"))  # Вывод: b'\xD0\x9F\xD1\x80\xD0\xB8\xD0\xB2\xD0\xB5\xD1\x82'

# Метод endswith(suffix[, start[, end]])
# Проверяет, заканчивается ли строка на суффикс.
example = "HelloWorld"
print(example.endswith("World"))  # Вывод: True

# Метод expandtabs([tabsize])
# Расширяет tabs до длины tabsize пробелов.
example = "\tHello\tworld\t"
print(example.expandtabs())  # Вывод: "    Hello    world    "

# Метод find(sub[, start[, end]])
# Находит первое вхождение подстроки sub в строке.
example = "HelloWorld"
print(example.find("o"))  # Вывод: 4

# Метод format(*args, **kwargs)
# Форматирует строку согласно позициям или именованным параметрам.
example = "Hello {name}"
print(example.format(name="World"))  # Вывод: "Hello World"

# Метод format_map(mapping)
# То же самое, что str.format(), но принимает словарь mapping.
example = "Hello {name}"
print(example.format_map({"name": "World"}))  # Вывод: "Hello World"

# Метод index(sub[, start[, end]])
# То же самое, что find(), но с исключением ValueError при пропуске.
example = "HelloWorld"
try:
    print(example.index("o"))  # Вывод: 4
except ValueError:
    print("Подстрока не найдена")

# Метод isalnum()
# Проверяет, состоит ли строка только из буквенно-цифровых символов.
example = "123Hello456"
print(example.isalnum())  # Вывод: False

# Метод isalpha()
# Проверяет, состоит ли строка только из буквенных символов.
example = "Hello"
print(example.isalpha())  # Вывод: True

# Метод isdecimal()
# Проверяет, состоит ли строка только из десятичных цифр.
example = "123.456"
print(example.isdecimal())  # Вывод: False

# Метод isdigit()
# Проверяет, состоит ли строка только из цифровых символов.
example = "123"
print(example.isdigit())  # Вывод: True

# Метод isidentifier()
# Проверяет, является ли строка допустимым идентификатором.
example = "my_variable"
print(example.isidentifier())  # Вывод: True

# Метод islower()
# Проверяет, состоит ли строка только из строчных букв.
example = "hello"
print(example.islower())  # Вывод: True

# Метод isnumeric()
# Проверяет, состоит ли строка только из числовых символов.
example = "123"
print(example.isnumeric())  # Вывод: True

# Метод isprintable()
# Проверяет, состоит ли строка только из печатных символов.
example = "Hello"
print(example.isprintable())  # Вывод: True

# Метод isspace()
# Проверяет, состоит ли строка только из пробельных символов.
example = "    "
print(example.isspace())  # Вывод: True

# Метод istitle()
# Проверяет, состоит ли строка только из титульных букв.
example = "Title Case Text"
print(example.istitle())  # Вывод: True

# Метод isupper()
# Проверяет, состоит ли строка только из заглавных букв.
example = "HELLO"
print(example.isupper())  # Вывод: True

# Метод join(iterable)
# Возвращает новую строку, где элементы iterable разделены данной строкой.
example = "+"
numbers = [1, 2, 3]
print(example.join(map(str, numbers)))  # Вывод: "1+2+3"

# Метод ljust(width[, fillchar])
# Возвращает строку, где строка дополнена слева до ширины width.
example = "Hello"
print(example.ljust(10, ""))  # Вывод: "Hello********"

# Метод lower()
# Преобразует строку в нижний регистр.
example = "Hello"
print(example.lower())  # Вывод: "hello"

# Метод lstrip([chars])
# Удаляет префикс из пробельных или указанных символов.
example = "    Hello    "
print(example.lstrip())  # Вывод: "Hello    "

# Метод maketrans(x[, y[, z]])
# Возвращает объект для транслитерации строк.
example = "АБВ"
translation = example.maketrans("АБВ", "abc")
print(example.translate(translation))  # Вывод: "abc"

# Метод partition(sep)
# Разделяет строку на три части: до первого вхождения sep, сам sep и после sep.
example = "Hello, World!"
sep = ","
print(example.partition(sep))  # Вывод: ('Hello', ',', ' World!')

# Метод replace(old, new[, count])
# Заменяет все вхождения подстроки old на new.
example = "Hello, World!"
print(example.replace(",", "."))  # Вывод: "Hello. World!"

# Метод rfind(sub[, start[, end]])
# Находит последнее вхождение подстроки sub в строке.
example = "HelloWorld"
print(example.rfind("o"))  # Вывод: 7

# Метод rindex(sub[, start[, end]])
# То же самое, что rfind(), но с исключением ValueError при пропуске.
example = "HelloWorld"
try:
    print(example.rindex("o"))  # Вывод: 7
except ValueError:
    print("Подстрока не найдена")

# Метод rjust(width[, fillchar])
# Возвращает строку, где строка дополнена справа до ширины width.
example = "Hello"
print(example.rjust(10, "*"))  # Вывод: "*****Hello"

# Метод rpartition(sep)
# Разделяет строку на три части: до последнего вхождения sep, сам sep и после sep.
example = "Hello, World!"
sep = ","
print(example.rpartition(sep))  # Вывод: ('Hello,', ',', ' World!')

# Метод rsplit([sep[, maxsplit]])
# Разделяет строку на список строк по разделителю sep.
example = "Hello, World!"
print(example.rsplit(","))  # Вывод: ['Hello', ' World!']

# Метод rstrip([chars])
# Удаляет суффикс из пробельных или указанных символов.
example = " Hello,"
print(example.rstrip())
