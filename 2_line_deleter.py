a=raw_input("Enter a keyword to lookfor:")
f=open("Test.txt","r")
d=open("out.txt","w")
while True:
	z=f.readline()
	if a in z:
		z=f.readline()
		continue
	if z=="":
		print "Done!"
		break
	d.write(z)
	z=f.readline()
	d.write(z)
d.close()
f.close()
