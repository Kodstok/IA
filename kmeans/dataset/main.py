import kmeans

tab_class = []

def open_dataset():
	fdata = open ("./dataset/iris/iris.data")
	data = []
	
	for row in fdata:
		row = row.rstrip().split(",") #on utilise les , comme des delimiteurs
		tab_class.append(row.pop())
		data.append(row)
	
	data.pop() # enleve la derniere ligne
	tab_class.pop()
	return data

if __name__ == "__main__": 
	data = open_dataset()

	kmeans.kmeans(data,3)