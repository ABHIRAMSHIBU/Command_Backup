f=open("a.txt","r")
def read_line():
	i=0
	while True:
		i+=1
		z=f.readline()
		if ("=-StArt-Wo!-=" in z):
			z=f.readline()
			break
		elif (i==100):
			return ("=-End-=","=-Error-=")
	a=z[:-1]
	b=f.readline()[:-1]
	return (a,b)
i=0
while True:
	a,b=read_line()
	if ("=-End-=" in a or "=-Error-=" in b):
		print "End of file"
		break
	i+=1
	print i
	a=a.split("bKpId-Name!=")
	b=b.split("bKpId-Loc!=")
	print "Name = "+a[1]
	print "Location = "+b[1]
#	c=input("Do you want to continue 1/0 :")
#	if(c==0):
#		break
