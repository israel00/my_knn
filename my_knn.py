from math import sqrt
from random import choice


def knn(k, neighbors, point):
	
	#distances
	d = []
	for n in neighbors:
		soma = 0
		for i in range(0,len(n[0])):
			soma += (n[0][i]-point[0][i])**2
		d.append([sqrt(soma), n[1]])
	
	#sorting distances
	flag=1
	while(flag!=0):
		flag=0
		for i in range(0,len(d)-1):
			if d[i][0]>d[i+1][0]:
				aux = d[i]
				d[i]=d[i+1]
				d[i+1]=aux
				flag += 1


	#dictionary with k nearest neighbors
	n_group = {}
	for i in range(0,k):
		if d[i][1] in n_group:
			n_group[d[i][1]] += 1
		else:
			n_group[d[i][1]] = 1

	
	bigger =  max(n_group, key=n_group.get)

	group_list = []
	
	for c in n_group:
		if n_group[c] == n_group[bigger]:
			group_list.append(c) 


	
	if len(group_list) == 1:
		return group_list[0]
	else:
		#sorting if there are two or more in the list
		return choice(group_list)
	

	'''
	Exemple:

	N = [[[0,1], 'a'], [[0,0], 'b'], [[1,1], 'c'], [[1,2], 'd'], [[2,2], 'e'], [[0,0], 'a'], [[0,0], 'b'], [[3,6], 'c'], [[9,5], 'd'], [[0,0.5], 'e']]
	k = 3
	x = [[0,0], ' ']

	knn(k, N, x)
	'''
