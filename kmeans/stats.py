def moyenne(tab):
    return sum(tab, 0.0) / len(tab)

def variance(tab):
    m=moyenne(tab)
    return moyenne([(x-m)**2 for x in tab])
def ecartype(tab):
    return variance(tab)**0.5

def getStats(data):
    dataB = []
    lgLine = len(data[0])
    for i in range(lgLine):
        dataB.append([])
    
    for line in data:
        index = 0
        for value in line:
            dataB[index].append(float(value))
            index= index +1
    finalData=[]
    index = 0
    for line in dataB:
        finalData.append([])
        finalData[index].append(index)
        finalData[index].append(round(moyenne(line),2))
        finalData[index].append(round(ecartype(line),2))
        index=index+1
    #NB: pas besoin d'inclure le min et max puisque les valeurs sont normalise
    return finalData  