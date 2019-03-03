import random
N = 23
N_rounds = 10000
up_bound = 366 #367

duplicate_count = 0

for i in range(N_rounds):
	dates = []

	for j in range(1,24):
		x = random.randint(1,366)
		dates.append(x)
		date_set = set(dates)

		if(len(dates)>len(date_set)):
			duplicate_count += 1
			break
	#print duplicate_count,"\n"

print "Pass_percentage = ",(duplicate_count*100)/N_rounds

