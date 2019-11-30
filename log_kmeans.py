# coding: utf-8
import random
from copy import deepcopy
from math import sqrt
from typing import Tuple

import numpy as np

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
                result = result + sqrt(pow(other.point[i] - self.point[i], 2))
            return result
        else:
            for i in range(len(self.point)):
                result = result + sqrt(pow(other.point[i], 2)) - sqrt(pow(self.point[i], 2))
            return result


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


if __name__ == '__main__':
    
    final_list = []  # объявление списка ответов
    i = 0  # колво повторений одного и того же элемента
    pr = 0  # номер предидущего элемента
    j = 0  # номер итерации
    temp = normal('ll2.csv', 0.5)  # Нормализация исходных данных
    all_dots = []
    for k in temp:
        all_dots.append(Dot(k, True))  # формирование списка исходных данных
    first_s_point = gen_rand_obj(all_dots, 3)  # Генерация первой тройки объектов
    pr = v_sum(all_dots, first_s_point)
    while True:  # основной цикл
        sec_s_point = gen_rand_obj(all_dots, 3)  # Генерация второй тройки объектов
        new_min, new_s_points = new_obj(all_dots, first_s_point, sec_s_point, pr)
        if new_min == pr:
            i = i + 1  # увиличеваем переменную, которая считает сколько раз нам выдали один и тот же ответ
        else:  # Если не равен, то обновляем первую тройку точек и обнуляем i
            i = 0
            pr = new_min
            first_s_point = new_s_points
        j += 1
        if i == 10:  # Кол-во попыток найти элемент меньше/Внесение в список минимальных элементов
            final_list.append(pr)
        if j == 50:  # ограничение по итерациям
            if pr not in final_list:
                final_list.append(deepcopy(pr))
            print(final_list)
            break
# 0.00012059920469122685, 0.0001780519359350554, 0.00011647178532747887
# 0.00010806844841518404  0.00010803597530276108
# [0.00011148587642821461, 0.00010955847194149846, 0.00010857841449466461]
