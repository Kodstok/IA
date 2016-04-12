from math import sqrt, pow
from random import randint
from cluster import Cluster
from decimal import Decimal
import operator

def distance_euclidienne(vecteur1, vecteur2):
	#on calcule la distance entre le vec1 et le vec2 pour chaque coordonnees
	distance = sqrt(sum(pow(float(vecteur1[i])-float(vecteur2[i]),2) for i in range(len(vecteur1)))) 
	return distance

def get_cluster_obs(clusters, r):	
	res = Cluster(-1, [])
	for c in clusters:
		for obs_row in c.observations:
			if obs_row == r:
				res.id = c.id
				res.centroide = c.centroide
				res.observations = c.observations
	return res

def virer(clusters,n):
	dist_centroide=[]
	for c in clusters:
		for obs in c.observations:
			dist_centroide.append([c, distance_euclidienne(obs, c.centroide)])  
		sorted(dist_centroide, key=operator.itemgetter(1), reverse = False) 
		for i in range((len(dist_centroide)*n)/100):
			dist_centroide.pop()
		dist_centroide = []
	return dist_centroide
def kmeans (data, k):
	# Cluster est un objet qui contient:
	# un id, un centroide, un tableau d'observations
	
	clusters = []
	dist_centroide = []
	avg_centroide = [0,0,0,0] 
	curr_avg_centroide = [0,0,0]
	old_avg_centroide = [0,0,0]
	#On choisit K observations aleatoires comme centroide
	# initialisation forcee
	# Le principe : On prend K observations aleatoires qui seront centroide de chaque cluster
	for i in range(k):
		clusters.append(Cluster(i, data[i]))
	
	# on remplit chaque clusters avec les points les plus proches	
	for obs in data:
		for c in clusters:
			# on stocke les differentes distances entre nos clusters et l'observation
			dist_centroide.append([c, distance_euclidienne(obs, c.centroide)]) 		 
		# Maintenant, il faut trier le tableau de sorte a savoir vers quel cluster on place notre observation
		best_cluster = sorted(dist_centroide, key=operator.itemgetter(1), reverse = False)[0]
		best_cluster[0].observations.append(obs)
		# on vide notre tableau de distance pour les prochaines analyses
		dist_centroide = []
	
	# Une fois arrive ici; la premiere etape est terminee
	# il faut maintenant : calculer le nouveau centroide de chaque cluster et refaire ce qu'on a fait
	
	end = True
	while end:
		for c in clusters:
			avg_centroide = []
			for val in c.observations:
				for i in range(len(val)):
					avg_centroide.append(0)
					avg_centroide[i] += float(val[i])
							
			for i in range(len(avg_centroide)):
				avg_centroide[i] /= len(c.observations)
				avg_centroide[i] = round(avg_centroide[i], 1)
			c.centroide = avg_centroide
			
			
		for i in range(k):		
			curr_avg_centroide[i] = clusters[i].centroide
		if curr_avg_centroide == old_avg_centroide:
			end = False
			
		for i in range(k):
			old_avg_centroide[i] = clusters[i].centroide
		
		for obs in data:
			for c in clusters:
				dist_centroide.append([c, distance_euclidienne(obs, c.centroide)]) 	
				
			old_cluster = get_cluster_obs(clusters, obs)
			best_cluster = sorted(dist_centroide, key=operator.itemgetter(1), reverse = False)[0]

			dist_centroide = []
			if best_cluster[0].id != old_cluster.id :
				best_cluster[0].observations.append(obs)
				old_cluster.observations.remove(obs)
	return clusters
