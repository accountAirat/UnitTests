import pytest

from Seminars.seminars.six.hw.ListAverage import ListAverage


@pytest.fixture
def list_average_instance():
    return ListAverage()


def test_average_empty_list(list_average_instance):
    assert list_average_instance.average([]) == 0.0


def test_average_single_element_list(list_average_instance):
    assert list_average_instance.average([5]) == 5.0


def test_average_general_case(list_average_instance):
    assert list_average_instance.average([1, 2, 3, 4, 5]) == 3.0


def test_compare_average_greater(list_average_instance):
    result = list_average_instance.compare_average([1, 2, 3], [1, 2, 2])
    assert result == "Первый список имеет большее среднее значение"


def test_compare_average_lesser(list_average_instance):
    result = list_average_instance.compare_average([1, 2, 3], [4, 5, 6])
    assert result == "Второй список имеет большее среднее значение"


def test_compare_average_equal(list_average_instance):
    result = list_average_instance.compare_average([1, 2, 3], [3, 2, 1])
    assert result == "Средние значения равны"

