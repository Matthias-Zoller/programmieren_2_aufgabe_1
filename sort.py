import numpy as np

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
    return data