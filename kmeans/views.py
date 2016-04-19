from django.shortcuts import render
from .forms import PostForm
from .models import Document
from django.http import HttpResponseRedirect
from stats import getStats
from normalize import normalize
import kmeans
import os
# Create your views here.
#-*- coding: utf-8 -*-
tab_class = []

def open_dataset(name):
	fdata = open ("media/documents/"+name)
	data = []
	
	for row in fdata:
		row = row.rstrip().split(",") #on utilise les , comme des delimiteurs
		#tab_class.append(row.pop())
		data.append(row)
	
	#data.pop() # enleve la derniere ligne
	#tab_class.pop()
	return data

def open_dataset_range(name,range):
	fdata = open ("media/documents/"+name)
	data = []
	
	for row in fdata:
		row = row.rstrip().split(",") #on utilise les , comme des delimiteurs
		#tab_class.append(row.pop())
		data.append(row)
	finaldata=[]
	for row in data:
		r=[]
		for i in range:
			r.append(row[i])
		finaldata.append(r)
	return finaldata

def default(request):
	return render(request,'kmeans/page1.html',{})
    

def page2(request):
	if request.method =="POST":
		print(request.POST)
		str1="media/documents/"
		str2=request.FILES['docfile'].name
		if os.path.isfile(str1+str2):
			os.remove(str1+str2)
		newdoc = Document(docfile = request.FILES['docfile'])
		newdoc.save()
		request.session['classes']=request.POST['classes']
		request.session['remove']=request.POST['remove']
		request.session['docfile']=request.FILES['docfile'].name
		colonne=range(3)
		data = open_dataset(request.session['docfile'])
		normalizedData=normalize(data)
		stats = getStats(normalizedData)
		return render(request,'kmeans/page2.html',{'colonne':colonne,'stats':stats})
	else:
		return render(request,'kmeans/page1.html',{})

def page3(request):
	if request.method =="POST":
		data_color = ['blue','red','green','yellow','burlywood','darkblue','darkmagenta','darkgray','chocolate','deeppink','khaki','indianred']
		print(request.POST)
		print(request.session['remove'])
		l = 3
		rng =[]
		for i in range(l):
			rng.append(int(request.POST[''+str(i)]))
		print(rng)
		data = open_dataset_range(request.session['docfile'],rng)
		normalizedData=normalize(data)
		k = kmeans.kmeans(normalizedData, int(request.session['classes']))
		print("remove :"+request.session['remove'])
		k=kmeans.remove_extreme(k,int(request.session['remove']))
		#for c in k:
		#	print(c.id)
		index=1
		rg = []
		for i in range(len(k)-1):
			row=[]
			row.append(index)
			
			row.append(data_color[index])
			index=index+1
			rg.append(row)
		centro=[]
		index =0
		for c in k:
			print("cluster id : "+str(c.id)+" centroide : " + str(c.centroide[0])+" ; "+str(c.centroide[1])+" ; "+str(c.centroide[2]))
			row =[]
			st = str(c.centroide[0])+" ; "+str(c.centroide[1])+" ; "+str(c.centroide[2])
			row.append(index)
			index=index+1
			row.append(st)
			centro.append(row)
		print(centro)
		return render(request,'kmeans/test3.html',{'k':k,'rg':rg,'data_color':data_color,'rng':rng,'centro':centro})
	else:
		print("page 3 POST == false")
		return render(request,'kmeans/page1.html',{})
