from math import sqrt, pow
from random import randint
from cluster import Cluster
import operator

def distance_euclidienne(vecteur1, vecteur2):
	#on calcule la distance entre le vec1 et le vec2 pour chaque coordonnees
	distance = sqrt(sum(pow(float(vecteur1[i])-float(vecteur2[i]),2) for i in range(len(vecteur1)))) 
	return distance


def kmeans (data, k):
	# Cluster est un objet qui contient:
	# un id, un centroide, un tableau d'observations
	
	clusters = []
	dist_centroide = []
	#On choisit K observations aleatoires comme centroide
	# initialisation forcee
	# Le principe : On prend K observations aleatoires qui seront centroide de chaque cluster
	for i in range(k):
		r = randint(0, len(data) - 1)
		clusters.append(Cluster(i, data[r]))
		data.remove(data[r])
	
	# on remplit chaque clusters avec les points les plus proches	
	for obs in data:
		for c in clusters:
			# on stocke les differentes distances entre nos clusters et l'observation
			dist_centroide.append([c, distance_euclidienne(obs, c.centroide)]) 
			 
		# Maintenant, il faut trier le tableau de sorte a savoir vers quel cluster on place notre observation
		best_cluster =  sorted(dist_centroide, key=operator.itemgetter(1), reverse = False)[0]
		best_cluster[0].observations.append(obs)
		# on retire chaque point analyses, sinon les clusters auront des observations communes !!		 
		data.remove(obs)
		# on vide notre tableau de distance pour les prochaines analyses
		dist_centroide = []
	
	# Une fois arrive ici; la premiere etape est terminee
	# il faut maintenant : calculer le nouveau centroide de chaque cluster et refaire ce qu'on a fait
	
	for c in clusters:
		print "Cluster numero", c.id, ", Observations :", c.observations
	
	
	