import os, sys, csv

path = 'DGL5_1.csv'

with open(path, 'rUb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	next(reader, None)
	total, interesting, empty = 0, 0, 0
	tn, tp, fp, fn = 0, 0, 0, 0
	for row in reader:
		total += 1
		if 'Y' in row[1] and 'Y' in row[2]:
			tp += 1
		elif 'N' in row[1] and 'N' in row[2]:
			tn += 1
		elif 'N' in row[1] and 'Y' in row[2]:
			fp += 1
		elif 'Y' in row[1] and 'N' in row[2]:
			fn += 1

		#count all interesting and empty images found by humans	
		if 'Y' in row[1]:
			interesting += 1 
		elif 'N' in row[1]:
			empty += 1

	print total
	print 'True Positive: %d' % tp
	print 'True Negative: %d' % tn
	print 'False Positive: %d' % fp
	print 'False Negative: %d' % fn

	print 'Human Processed Interesting: %d' % interesting
	print 'Human Processed Empty: %d' % empty