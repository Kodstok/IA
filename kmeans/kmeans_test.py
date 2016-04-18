import unittest
import random
import kmeans
import main
import normalize

class KmeansTest(unittest.TestCase):
	
	def setUp(self):
		pass

	def testKMean(self):
		print("### Test du nombre d'observations de KMeans ###")
		dataLines = 0
		data=main.open_dataset()
		dat=normalize.normalize(data)
		#kmeans
		clusters=kmeans.kmeans(dat, 2)
		
		#nombre de lignes dans le dataset
		for row in data:
			if len(row) > 0:
				dataLines += 1
		
		#regarde si le nombre d observations du dateset est maintenu
		totalObsNb = 0
		for clusterNb in range(len(clusters)):
			clus = clusters [clusterNb]
			totalObsNb += len(clus.observations)
			
		# TEST - verifie si le nombre de points de tous les clusters est egal au nombre de ligne du dataset
		self.assertEqual (totalObsNb, dataLines, "Nombre d'observations du dataset different du resultat")
		
		print("### Test de la similitude des observations de KMeans ###")
		#verifie si toutes les entrees du dataset sont gardees
		for entry in dat:
			bool = False
			# pour chaque cluster
			for clusterNb in range(len(clusters)):
				clus = clusters[clusterNb]
				#pour chaque element du cluster
				for elems_clus in range(len(clus.observations)):
					if clus.observations[elems_clus] == entry:
						bool = True
						
			# TEST - l'entree selectionne a ete conserve dans les clusters finaux
			self.assertTrue(bool, "Observations du dataset differentes du resultat")
		
		print("### Test d'existance de centroides ###")
		# verifie l'existance de centroides
		for clusterNb in range(len(clusters)):
			clus = clusters[clusterNb]
			# TEST - il existe au moins un centroide
			self.assertTrue(len(clus.centroide) > 0, "Pas de centroide detecte")
			
		# verifie la validite des centroides
		print("### Test de validite des centroides ###")
		for i in range(len(clusters)):
			clus = clusters[i]
			centro = clus.centroide
			obs = clus.observations
			for j in range(3):
				tmp = 0
				for i in range(len(obs)):
					try:
						tmp += float(obs[i][j])
					except ValueError:
						pass
				try:
					value = float(centro[j])
					self.assertTrue(tmp/len(obs) == value, "Centroide non valide")
				except ValueError:
						pass

if __name__ == "__main__":
    unittest.main()