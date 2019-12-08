# coding: utf-8
import random
from copy import deepcopy
from typing import Any, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from norm import normal


class Dot:
    """
    Класс точки
    Содержит кординаты и данные об используемой метрике
    TODO переделать
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
        :return:
        """
        return len(self.spec_points)
    
    def __getitem__(self, item: int) -> Dot:
        return self.spec_points[item]


def v_sum(all_dots: list, special_dots: SpecialPoint) -> float:
    """
    
    :type all_dots: list
    :param all_dots:
    :param special_dots:
    :return:
    """
    result = 0
    for i in special_dots.spec_points:
        for k in all_dots:
            if i != k:
                result = result + (i + k)
    return result


def new_obj(all_dots: list, first: SpecialPoint, sec: SpecialPoint, min_sum_now: int) -> Tuple[int, list]:
    """
    :param min_sum_now: Минимальная сумма на начало прогона
    :param all_dots: Все точки
    :param first: Первый объект
    :param sec: Второй объект
    :return: Минимальная сумма и наилучшее сочитание компонентов первого и второго объекта
    """
    sp_len = len(first)
    test_list = []
    
    for k in range(sp_len):
        if random.random() < 0.5:
            test_list.append(sec[k])
        else:
            test_list.append(first[k])
    new_sum = v_sum(all_dots, SpecialPoint(test_list))
    if new_sum < min_sum_now:
        min_sum_now = new_sum
    return min_sum_now, test_list


def gen_rand_obj(dots: list, k_amount) -> SpecialPoint:
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


def k_medoid(k_amount: int = 3, iteration_constraint: int = 100, metryx_type: bool = False, file_path: str = None,
             n_cof: float = None) -> Tuple[Union[np.ndarray, Any], Union[SpecialPoint, list]]:
    """
    
    :param k_amount: Кол-во медоидов
    :param iteration_constraint: Кол-во итераций. По умолчанию 50
    :param metryx_type: Тип метрики, по умолчанию Евклидова
    :param file_path: Путь к файлу. При отсутствии срабатывают случайные значения
    :param n_cof: коофицент нормализации. Работает только при наличии пути файла
    :return: массив точек с параметром k_class указывающий на пренадлежность к классу и массив медоидов
    """
    if not file_path:
        temp = np.random.randint(-100, 100, (1000, 2))
        data = np.array([Dot(i, metryx_type) for i in temp])
    else:
        temp = np.array(pd.read_csv(file_path))
        data = np.array([Dot(i, metryx_type) for i in temp])
        if n_cof:
            data = normal(data, n_cof)
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
    return deepcopy(data), deepcopy(first_s_point)


if __name__ == '__main__':
    colors = ['red', 'green', 'blue', 'black', 'orange', 'yellow']
    ax = plt.subplots(figsize=(10, 10))[1]
    result = k_medoid(iteration_constraint=200, k_amount=3,
                      file_path='irisDataNoHeadDotComma.csv')  # чтобы использовать случайные значения нужно удалить "file_path='irisDataNoHeadDotComma.csv'"
    for i in result[0]:
        ax.scatter(i[0], i[1], color=colors[int(i.k_class)])
    for i in result[1]:
        ax.scatter(i[0], i[1], color=colors[int(i.k_class)], lw=10, marker='^')
    plt.show()
