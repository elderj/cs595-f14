from math import sqrt


data = raw_input("Enter all sample elements:")

print "To calculate variance and standard deviation first find the"
print "average of the dataset.  Take the average and subtract it  "
print "from each number in the dataset to get the deviations.     "
print "Square each deviation and add them together to get variance"
print "Take the Square root of both sides for std deviation       "

l = map(int, data.split())


total = 0
i=0
for element in l:
	total = total + l[i]
	i = i+1



print "The total friends of friends is ", total
print "The number of entries is ", len(l)

mean = float(total)/len(l)




print "The mean is ", mean

variance=0
i=0
for element in l:
	dev = l[i] - mean
	dev = dev * dev
	variance = variance + dev


print "The Variance is ", variance
print "The Standard Deviation is", sqrt(variance)
	
