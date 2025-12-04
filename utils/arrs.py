"""Функции для работы с массивами"""


def get(array, index, default=None):
    """
    Извлекает из списка значение по указанному индексу, если индекс существует.
    Если индекс не существует, возвращает значение по умолчанию.
    Функция работает только с неотрицательными индексами.

    :param array: исходный список
    :param index: индекс извлекаемого элемента
    :param default: значение по умолчанию
    :return: значение по индексу или значение по умолчанию
    """
    if 0 <= index < len(array):
        return array[index]
    return default


def my_slice(coll, start=None, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
                  start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
                Если индекс отрицательный, end указывает смещение от конца списка.
                По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    if start is None:
        start = 0
    elif start < 0:
        start = max(length + start, 0)

    if end is None:
        end = length
    elif end < 0:
        end = length + end
    elif end > length:
        end = length

    start = max(0, min(start, length))
    end = max(0, min(end, length))

    if start >= end:
        return []

    return coll[start:end]