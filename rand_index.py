def rand_index(data, et_data):
    classes = data[-1]
    a = b = c = d = 0
    for i in range(len(data[-1])):
        for j in range(len(data[-1])):
            if classes[i] == classes[j]:
                if et_data[i] == et_data[j]:
                    a += 1
                else:
                    c += 1
            else:
                if et_data[i] != et_data[j]:
                    b += 1
                else:
                    d += 1
    return (a + b) / (a + b + c + d)


if __name__ == '__main__':
    import pandas as pd

    data = [pd.read_csv('result.csv')['class'].to_list()]
    et = pd.read_csv('irisDataNoHeadCommaSemititles.csv')['4'].to_list()
    x = rand_index(data, et)
