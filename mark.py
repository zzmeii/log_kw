import numpy as np
from sklearn.cluster import KMeans


class Dot:
    """
    Класс точки
    Содержит кординаты и данные об используемой метрике
    DONE переделать
    """

    def __init__(self, cords: list, k_class: int = None):
        """
        Принимаеи кординаты и bool, если True, то используется манхеттенская метрика, иначе, евклидова
        :param cords:
        :param m_type:
        """
        self.k_class = k_class
        self.point = np.array(cords.copy())

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

    def __add__(self, other):
        """
        Перегрузка сложения

        :param other:
        :return:
        """
        res = [0 for i in range(len(self.point))]
        for i in range(len(self.point)):
            res[i] = self[i] + other[i]
        return Dot(res, True)

    def __getitem__(self, item: int) -> int:
        return self.point[item]

    def __sub__(self, other):

        res = [0 for i in range(len(self.point))]
        for i in range(len(self.point)):
            res[i] = self[i] - other[i]
        return Dot(res, True)

    def __float__(self):
        res = self[0]
        for i in range(1, len(self.point)):
            res *= self[i]
        return res


def mark(data):
    dot_list = []
    for i in range(len(data[0])):
        dot_list.append(Dot(data[0][i], k_class=data[1][i]))
    res = 0
    for i in range(max(data[1])):
        temp_mean = []
        for j in dot_list:
            if j.k_class == i:
                temp_mean.append(j)
        for j in range(len(temp_mean)):
            temp_mean[j] = float(temp_mean[j])
        mean = np.mean(temp_mean)
        res += sum([j - mean for j in temp_mean]) ** 2
    return res
