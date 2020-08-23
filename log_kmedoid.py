import random
from typing import Tuple, List, Union

from test import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Dot:
    """
    Класс точки
    Содержит кординаты и данные об используемой метрике
    DONE переделать
    """

    def __init__(self, cords: list, m_type: bool):
        """
        Принимаеи кординаты и bool, если True, то используется манхеттенская метрика, иначе, евклидова
        :param cords:
        :param m_type:
        """
        self.k_class = None
        self.point = np.array(cords.copy())
        self.m_type = m_type
        self.medoid = False

    def __eq__(self, other) -> bool:
        """
        Перегрузка эквиваленции
        
        :param other:
        :return:
        """
        for i in range(len(self.point)):
            if self.point[i] == other.point[i]:
                pass
            else:
                return False
        return True

    def __add__(self, other) -> float:
        """
        Перегрузка сложения
        
        :param other:
        :return:
        """
        result = 0
        if self.m_type:
            for i in range(len(self.point)):
                result = result + abs(other.point[i] - self.point[i])
            return result
        else:
            for i in range(len(self.point)):
                result = result + pow(other.point[i] - self.point[i], 2)
        return np.sqrt(result)

    def __getitem__(self, item: int) -> int:
        return self.point[item]


class SpecialPoint:
    """
    Класс содержащий специальные точки.
    
    """

    def __init__(self, point):
        self.spec_points = point.copy()

    def __eq__(self, other) -> bool:
        """
       Перегрузка эквиваленции

       :param other:
       :return:
        """
        m = 0
        for i in self.spec_points:
            for k in other.spec_points:
                if i == k:
                    m += 1
        if m < len(self.spec_points):
            return True
        else:
            return False

    def __len__(self) -> int:
        """
        Пеоегрузка функции len()
        :return: int
        """
        return len(self.spec_points)

    def __getitem__(self, item: int) -> Dot:
        return self.spec_points[item]


def v_sum(all_dots, special_dots: SpecialPoint) -> float:
    """
    :type all_dots
    :param all_dots:
    :param special_dots:
    :return:
    """
    result = 0

    for i in all_dots:
        temp = []
        if i not in special_dots.spec_points:
            for k in special_dots.spec_points:
                temp.append(i + k)
            result = result + min(temp)

    return result


def new_obj(all_dots: np.ndarray, first: SpecialPoint, sec: SpecialPoint, min_sum_now: int) -> Tuple[int, list]:
    """
    :param min_sum_now: Минимальная сумма на начало прогона
    :param all_dots: Все точки
    :param first: Первый объект
    :param sec: Второй объект
    :return: Минимальная сумма и наилучшее сочитание компонентов первого и второго объекта
    """
    sp_len = len(first)
    temp_list = []

    for k in range(sp_len):
        if random.random() < 0.5 and sec[k] not in temp_list:
            temp_list.append(sec[k])
        elif first[k] not in temp_list:
            temp_list.append(first[k])
        else:
            temp_list.append(sec[k])
    new_sum = v_sum(all_dots, SpecialPoint(temp_list))
    if new_sum < min_sum_now:
        min_sum_now = new_sum
    return min_sum_now, temp_list


def gen_rand_obj(dots: np.ndarray, k_amount) -> SpecialPoint:
    """
    Генерирует объект на основе трех случайных точек
    DONE сделать универсальной для любого кол-ва точек
    :param k_amount: Необходимое количество специальных точек
    :param dots: Все точки
    :return:
    """
    first = []
    while True:
        point = random.randint(0, len(dots) - 1)
        if point not in first:
            first.append(point)
        if len(first) == k_amount:
            return SpecialPoint([dots[i] for i in first])


def convert_to_table(initial) -> List[list]:
    res = [[], [], []]
    for i in initial:
        res[0].append(list(i.point))
        res[1].append(i.k_class)
        res[2].append(i.medoid)
    return res


def k_medoid(origin_data, k_amount: int = 3, iteration_constraint: int = 300, metrics_type: bool = False,
             ret_table=True) -> Union[List[list], np.ndarray]:
    """

    :param ret_table: Возвращает массив
    :param origin_data: Уже предобработанные данные. Обязательный аргумент
    :param k_amount: Кол-во медоидов
    :param iteration_constraint: Кол-во итераций. По умолчанию 300
    :param metrics_type: Тип метрики, по умолчанию Евклидова
    :return: массив точек с параметром k_class указывающий на пренадлежность к классу и массив медоидов
    """

    temp = origin_data
    data = np.array([Dot(i, metrics_type) for i in temp])

    first_s_point = gen_rand_obj(data, k_amount)  # Генерация первой тройки объектов
    pr = v_sum(data, first_s_point)
    for _ in range(iteration_constraint):
        sec_s_point = gen_rand_obj(data, k_amount)  # Генерация второй тройки объектов
        new_min, new_s_points = new_obj(data, first_s_point, sec_s_point, pr)
        if new_min != pr:
            pr = new_min
            first_s_point = new_s_points
    for i in data:
        min_sum = -1
        k_class = 0
        for k in first_s_point:
            if i + k < min_sum or min_sum < 0:
                k_class = first_s_point.index(k)
                min_sum = i + k
        i.k_class = k_class
    for i in first_s_point:
        i.medoid = True
    return convert_to_table(data) if ret_table else data


if __name__ == '__main__':
    # data = np.array(pd.read_csv('irisDataNoHeadDotComma.csv', header=None))
    colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']
    ax = plt.subplots()[1]
    result = k_medoid(data[0], iteration_constraint=300, k_amount=3, metrics_type=False)
    print(result)
    for i in range(len(result[1])):
        ax.scatter(result[0][i][0], result[0][i][1], color=colors[result[1][i]])
    plt.show()
