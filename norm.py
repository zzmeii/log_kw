# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np


def change(data: list):
    if data is not list:
        return
    end_data = []
    __len = len(data[0])
    for i in range(__len):
        end_data.append([])
    for i in range(__len):
        for k in range(len(data)):
            end_data[i].append(data[k][i])
    return end_data


def normal(data, arg):
    """
    функция отдельно от класса
    
    :param data:
    :param arg: аргумент для нормировки
    :return:
    """
    
    end_data = []
    for i in range(0, len(data)):  # Цикл перебирающий столбцы
        end_data.append([])
        center = (min(data[i]) + min(data[i])) / 2
        for k in range(1, len(data[i])):  # Цикл перебирающий строки
            xik = 1 / (np.exp((arg * (data[i][k] - center))) + 1)
            end_data[i].append(xik)
    return np.array(end_data)


if __name__ == '__main__':
    plt.plot(normal('ll2.csv', 0.2))
    plt.show()
