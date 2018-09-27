# 載入準備好的工具
import sys
sys.path.append('.prepared')
import pla as prepared
import numpy as np

# 重置預先準備好的 PLA 示範模型
prepared.reset()

# 更新該 PLA 模型
prepared.update()

# 繪製該 PLA 模型
prepared.plot()

# 執行多次觀察 PLA 模型迭代的過程，收斂後可以執行上面程式區段執行重置模型

def sign(x):
    if(x>0):
        return 1
    else:
        return -1

def pla():
    dimssion = 4
    # TODO: start coding here...
    # the first thing is to read `pla.dat`
    f  = open('./pla.dat', 'r')
    #print(f.read())

    inputdata = []
    data = [] #每個點的位置
    label = [] #每個點的類別
    inputdata = f.read().split('\n')
    #存成二維list
    for i in range(0,len(inputdata)-1):
        data.append([])
        line = inputdata[i].split(" ")
        data[i].append(1) #補常數
        for value in range(0,dimssion):
            data[i].append(float(line[value]))
        data[i] = np.array(data[i])
        label.append(int(line[4]))

    w = data[0]
    stop = True
    while stop:
        stop = False
        for item in range(0,len(data)):
            #有錯的時候 更新線
            if sign(np.dot(w,data[item])) != label[item]:
                w += label[item]*data[item]
                stop = True

    print("Q56074019的ANS:\n",w)

if True: # TODO: change `False` to `True` once you finish `pla()`
    pla()
    print("助教的答案")
    prepared.demo()
else:
    prepared.demo()