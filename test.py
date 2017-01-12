import pickle
db_name="a.txt"
db_temp="temp.txt"
def append(z,y):
#	class test:
#		def __init__(self, name, location, date="Null") :
#			self.name=name
#			self.date=date
#			self.location=location
	f=open(db_name,"a")
	f.write("=-StArt-Wo!-=\n")
#	f.write("bKpId-Id!="+z+"\n")
	f.write("bKpId-Name!="+z+"\n")
#	f.write("bKpId-Code!="+z+"\n")
	f.write("bKpId-Loc!="+y+"\n")
	f.write("=-EnD;-;-=\n")
	f.close()
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
def db_append():
	while True:
		append(raw_input("Enter a name :"), raw_input("Enter a location :"))
		c=input("Do u want to enter again 1/0 :")
		if c==0:
			break
def db_dump():
	i=0 
	global f
	f=open(db_name,"r")
	while True:
		a,b=read_line()
		if ("=-End-=" in a or "=-Error-=" in b):
			print "End of file"
			break
		i+=1
		print "Id=",i
		a=a.split("bKpId-Name!=")
		b=b.split("bKpId-Loc!=")
		print "Name = "+a[1]
		print "Location = "+b[1]
def begin_find(f,z):
	while ("=-StArt-Wo!-=" in z):
			return(pos,f.readline())
	pos=f.tell()
	f.readline()
def delete():
	a=raw_input("Enter the name or location:")
	f=open(db_name,"r")
	d=open(db_temp,"w")
	while True:
		pos=f.tell()
		z=f.readline()
		begin_find(f,z)
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
db_append()
db_dump()
