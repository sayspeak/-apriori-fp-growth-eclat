# -*- coding: utf-8 -*-
from FPgrowth import fp_growth
from Apriori import apriori_zc
from Eclat import eclat_zc
import matplotlib.pyplot as plt
import time
from matplotlib import pyplot
import matplotlib

def plot_pic(x_value, y_value, title, x_name):
    plot1 = plt.plot(x_value, y_value[0], 'r', label='Kulc')  # use pylab to plot x and y
    plot2 = plt.plot(x_value, y_value[1], 'g', label='IR')  # use pylab to plot x and y
    # plot3 = plt.plot(x_value, y_value[2], 'b', label='Apriori')  # use pylab to plot x and y
    plt.title(title)  # give plot a title
    plt.xlabel(x_name)  # make axis labels
    plt.ylabel('value ')
    plt.legend(loc='upper right')  # make legend

    plt.show()  # show the plot on the screen
'''
def loadDblpData(inFile, flag=' ', row_num=1):

    #加载dblp的数据
    #:param inFile:
    #:return:

    file = open(inFile)
    dataSetDict = {}
    dataSet = []
    count = 0
    for line in file.readlines():
        print(line)
        # if count > row_num:
        #     break
        line = line.strip().split(':')
        line = line[1].strip().split()
        dataSet.append(line)
        dataLine = [word for word in line]
        dataSetDict[frozenset(dataLine)] = dataSetDict.get(frozenset(dataLine), 0) + 1
        count += 1
    return dataSetDict, dataSet
'''
def test_fp_growth(minSup, dataSetDict, dataSet):
    freqItems = fp_growth(dataSetDict, minSup)
    freqItems = sorted(freqItems.items(), key=lambda item: item[1])
    return freqItems


def test_apriori(minSup, dataSetDict, dataSet):
    freqItems = apriori_zc(dataSet, dataSetDict, minSup)
    freqItems = sorted(freqItems.items(), key=lambda item: item[1])
    return freqItems


def test_eclat(minSup, dataSetDict, dataSet):
    freqItems = eclat_zc(dataSet, minSup)
    freqItems = sorted(freqItems.items(), key=lambda item: item[1])
    return freqItems
def do_experiment_min_support():
    file = open('/Users/apple/PycharmProjects/Apriori/freqpattern-master/datasets/connectPro.txt')
    dataSetDict = {}
    dataSet = []
    for line in file.readlines():
        curLine = line.strip().split(":")
        # floatLine=map(float,curLine)#这里使用的是map函数直接把数据转化成为float类型
        dataSet.append(curLine)
        dataLine = [word for word in line]
        dataSetDict[frozenset(dataLine)] = dataSetDict.get(frozenset(dataLine), 0) + 1

    data_name = 'connectPro_0'
    x_name = "Min_Support"
    data_num = 1500
    minSup = data_num / 6

    #dataSetDict, dataSet = loadDblpData(inFile='/Users/apple/PycharmProjects/Apriori/freqpattern-master/datasets/unixData8_pro.txt', flag=',', row_num=data_num)
    step = minSup / 5  # #################################################################
    all_time = []
    x_value = []
    for k in range(5):

        x_value.append(minSup)  # #################################################################
        if minSup < 0:  # #################################################################
            break
        time_fp = 0
        time_et = 0
        time_ap = 0
        freqItems_fp = {}
        freqItems_eclat = {}
        freqItems_ap = {}
        for i in range(10):
            ticks0 = time.time()
            freqItems_fp = test_fp_growth(minSup, dataSetDict, dataSet)
            time_fp += time.time() - ticks0
            ticks0 = time.time()
            freqItems_eclat = test_eclat(minSup, dataSetDict, dataSet)
            time_et += time.time() - ticks0
            ticks0 = time.time()
            freqItems_ap = test_apriori(minSup, dataSetDict, dataSet)
            time_ap += time.time() - ticks0
        print("minSup :", minSup, "      data_num :", data_num, \
            "  freqItems_fp:", len(freqItems_fp), " freqItems_eclat:", len(freqItems_eclat), "  freqItems_ap:", len(
            freqItems_ap))
        print("fp_growth:", time_fp , "       eclat:", time_et / 10, "      apriori:", time_ap / 10)
        # print_freqItems("show", freqItems_eclat)
        minSup -= step   # #################################################################
        use_time = [time_fp / 10, time_et / 10, time_ap / 10]
        all_time.append(use_time)
        # print use_time
    y_value = []
    for i in range(len(all_time[0])):
        tmp = []
        for j in range(len(all_time)):
            tmp.append(all_time[j][i])
        y_value.append(tmp)
    plot_pic(x_value, y_value, data_name, x_name)
    return x_value, y_value
def do_experiment_data_size():
    file = open('/Users/apple/PycharmProjects/Apriori/freqpattern-master/datasets/connectPro.txt')
    dataSetDict = {}
    dataSet = []
    for line in file.readlines():
        curLine = line.strip().split(":")
        # floatLine=map(float,curLine)#这里使用的是map函数直接把数据转化成为float类型
        dataSet.append(curLine)
        dataLine = [word for word in line]
        dataSetDict[frozenset(dataLine)] = dataSetDict.get(frozenset(dataLine), 0) + 1
    data_name = 'connectPro_1'
    x_name = "Data_Size"
    data_num = 3000

    step = data_num / 5  # #################################################################
    all_time = []
    x_value = []
    for k in range(5):
        minSup = data_num * 0.010
        #dataSetDict, dataSet = loadDblpData(open("dataSet/"+data_name), ' ', data_num)
        x_value.append(data_num)  # #################################################################
        if data_num < 0:  # #################################################################
            break
        time_fp = 0
        time_et = 0
        time_ap = 0
        freqItems_fp = {}
        freqItems_eclat = {}
        freqItems_ap = {}
        for i in range(2):
            ticks0 = time.time()
            freqItems_fp = test_fp_growth(minSup, dataSetDict, dataSet)
            time_fp += time.time() - ticks0
            ticks0 = time.time()
            freqItems_eclat = test_eclat(minSup, dataSetDict, dataSet)
            time_et += time.time() - ticks0
            ticks0 = time.time()
            # freqItems_ap = test_apriori(minSup, dataSetDict, dataSet)
            # time_ap += time.time() - ticks0
        print("minSup :", minSup, "      data_num :", data_num, \
            "  freqItems_fp:", len(freqItems_fp), " freqItems_eclat:", len(freqItems_eclat), "  freqItems_ap:", len(freqItems_ap))
        print("fp_growth:", time_fp / 10, "       eclat:", time_et / 10, "      apriori:", time_ap / 10)
        # print_freqItems("show", freqItems_eclat)
        data_num -= step   # #################################################################
        use_time = [time_fp / 10, time_et / 10, time_ap / 10]
        all_time.append(use_time)
        # print use_time

    y_value = []
    for i in range(len(all_time[0])):
        tmp = []
        for j in range(len(all_time)):
            tmp.append(all_time[j][i])
        y_value.append(tmp)
    plot_pic(x_value, y_value, data_name, x_name)
    return x_value, y_value

if __name__ == '__main__':
     x_value, y_value = do_experiment_min_support()
     x_value, y_value = do_experiment_data_size()
     #do_test()