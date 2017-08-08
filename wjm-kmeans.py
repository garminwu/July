from numpy import *
#支持函数

#数据集预处理函数
def dataDeal(filename):
	f = open(filename)
	dataSet = []
	for i in f.readlines():
		line = i.strip().split('\t')
		linenew =list(map(float,line))
		dataSet.append(linenew)
	return dataSet

#欧式距离计算函数
def distance(vec1,vec2):
	return sqrt(sum(power(vec2-vec1,2)))

#生成随机质心
def heart(dataSet,k):
	d = shape(dataSet)[1]
	centroids = mat(zeros((k,d)))
	for i in range(d):
		mini = min(dataSet[:,i])
		rangei = float(max(dataSet[:,i]) - mini)  # first error  add float
		centroids[:,i] = mat(mini + rangei * random.rand(k,1))
		# centroids[:, j] = mat(minJ + rangeJ * random.rand(k, 1))
	return centroids


#支持函数end

#kMeans 函数开始
def kMeans(dataSet,k,distance,heart):
	n = shape(dataSet)[0]
	centroids = heart(dataSet,k)
	cluster_inf = mat(zeros((n,2)))
	sign = True
	while sign:
		sign = False
		for i in range(n):
			dist = inf
			minIndex = -1
			for j in range(k):
				a = distance(dataSet[i,:],centroids[j,:])  # error second
				#a = distance(centroids[j,:],dataSet[i,:])
				if a<dist: # error
					dist=a
					minIndex = j # error
			if cluster_inf[i, 0] != minIndex: # error
				sign = True # error
			cluster_inf[i, :] = minIndex, dist ** 2 # error
		# print(cluster_inf)
		for a in range(k):
			# load = []
			# for b in range(n):
			# 	if cluster_inf[b,0]==a:
			# 		load.append(dataSet[j].tolist()[0])
			# load = mat(load)
			load = dataSet[nonzero(cluster_inf[:, 0].A == a)[0]]
			centroids[a,:] = mean(load,axis=0)
	#return centroids,cluster_inf
	print(centroids)
	print("="*50)
	print(cluster_inf)

dataSet = mat(dataDeal('./testSet2.txt'))

kMeans(dataSet,4,distance,heart)

