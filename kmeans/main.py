import kmeans
import normalize
import stats
import time

tab_class = []
def comp(v1, v2):
	if v1[2]<v2[2]:
		return -1
	elif v1[2]>v2[2]:
		return 1
	else:
		return 0

def open_dataset():
	fdata = open ("./dataset/iris/spambase.data")
	data = []
	
	for row in fdata:
		row = row.rstrip().split(",") #on utilise les , comme des delimiteurs
		tab_class.append(row.pop())
		data.append(row)
	
	data.pop() # enleve la derniere ligne
	tab_class.pop()
	finaldata=[]
	for row in data:
		r=[]
		r.append(row[2])#pour l'instant c'est ici que l'on chsoie les colonne 
		r.append(row[18])
		r.append(row[20])
		finaldata.append(r)
	return finaldata

if __name__ == "__main__": 
	tmps1=time.clock()
	data = open_dataset()
	
	dat=normalize.normalize(data)
	f=kmeans.kmeans(dat, 2)
	b=kmeans.virer(f, 3)
	stat = stats.getStats(dat)
	stat.sort(cmp=comp)
	for row in stat:
		print row
	print b
	for c in b:
		print(len(c.observations))
	tmps2=time.clock()
	print "Temps d'execution = %d\n" %(tmps2-tmps1)