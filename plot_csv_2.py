import numpy as np
import sys
import matplotlib.pyplot as plt

m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]
mt=m.T

if len(sys.argv)==2:
  v1=mt[1];v2=mt[2]
elif len(sys.argv)==3:
  v1=mt[1][int(sys.argv[2]):len(mt[1])];v2=mt[2][int(sys.argv[2]):len(mt[2])]
else:
  v1=mt[1][int(sys.argv[2]):int(sys.argv[3])];v2=mt[2][int(sys.argv[2]):int(sys.argv[3])]

print("length of array="+str(len(v1)))
x=range(len(v1)) #plot array
plt.plot(x,v1)
plt.show()
x=range(len(v2)) #plot array
plt.plot(x,v2)
plt.show()

exit()