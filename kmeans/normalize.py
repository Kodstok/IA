'''
Created on 1 avr. 2016

@author: Kodstok
'''

def normalize(data):
    dataB = []
    lgLine = len(data[0])
    for i in range(lgLine):
        dataB.append([])
    
    for line in data:
        index = 0
        for value in line:
            dataB[index].append(float(value))
            index= index +1
    i=0
    for line in dataB:
        j = 0
        Vmin = min(line)
        Vmax = max(line)  
        for val in line:
            dataB[i][j] = ((val - Vmin)/(Vmax - Vmin))
            j=j+1
        i = i+1
    finalData=[]
    for i in range(len(dataB[0])):
        line = []
        for j in range(lgLine):
            line.append(dataB[j][i])
        finalData.append(line)
    return finalData