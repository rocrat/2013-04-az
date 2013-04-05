import sys
import screed

filename = sys.argv[1]
print filename

#for record in screed.open(filename):
#	print record
#	break
count = 0
for record in screed.open(filename):
	print record['sequence']
	print count
	count +=1
	if count>=10:
		break
	#this works
	