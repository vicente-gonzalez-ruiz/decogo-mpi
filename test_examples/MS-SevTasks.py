from mpi4py import MPI
import random
import sys

#-------------
def fAdd(a,b):
	return a+b

#-------------
def fSub(a,b):
	return a-b

#-------------
def fMul(a,b):
	return a*b

#------------- 
def fDiv(a,b):
	return a/b


#-------------
#-------------
commMPI = MPI.COMM_WORLD
rankMPI = MPI.COMM_WORLD.Get_rank()
nameMPI = MPI.Get_processor_name()
sizeMPI = MPI.COMM_WORLD.Get_size()


if sizeMPI<2:
	if (rankMPI==0):
		print("The number of proceses should be at least 2");
	sys.exit()

#print("Process",rankMPI,"/",sizeMPI,"in",nameMPI)
#sys.stdout.flush()		#to flush all queued prints.


#Define tag values depending of the function to perform
TagAdd=0
TagSub=1
TagMul=2
TagDiv=3
TagRes=4
TagEnd=5

#Define set operations mumber/function/symbol
OperNumb=[TagAdd,TagSub,TagMul,TagDiv]
Operfunc={TagAdd:fAdd, TagSub:fSub, TagMul:fMul, TagDiv:fDiv}
OperSymb={TagAdd:"+", TagSub:"-", TagMul:"*", TagDiv:"/"}


if rankMPI == 0: 	#I am master
	ListSize=100	#size of the list of operations
	List=[]

	#Generate a list of [a,b,oper,res] -> a oper b = res.
	for i in range (ListSize):
		List.append([i,i+1,random.choice(OperNumb),None])
		print(i,":",List[i][0],OperSymb[List[i][2]],List[i][1],"=",List[i][3])
	print("----------------------------------")
	sys.stdout.flush()

	NSend=0		#Sent operations to slaves from the List
	PendRec=0	#How many receives are pending.

	#Feed slaves 
	SlaveId=1;
	while PendRec<sizeMPI-1 and NSend<ListSize:
		dataMS=[NSend,List[NSend][0],List[NSend][1]]	#data from Master: (NSend,a,b)
		commMPI.send(dataMS,dest=SlaveId,tag=List[NSend][2]) #tag shows the oper to do (a oper b)
		NSend+=1
		PendRec+=1
		SlaveId+=1

	#receive from slave and feed it again
	while PendRec:
		dataSL=commMPI.recv(source=MPI.ANY_SOURCE,tag=TagRes) #data from slave (i,res,rank)
		PendRec-=1
		List[dataSL[0]][3]=dataSL[1]
		if NSend<ListSize:
			dataMS=[NSend,List[NSend][0],List[NSend][1]]	#data from Master (NSend,a,b)
			commMPI.send(dataMS,dest=dataSL[2],tag=List[NSend][2]) #tag shows the oper to do (a oper b)
			NSend+=1
			PendRec+=1


	#All work done -> sent a terminate message to all workers
	for i in range(1,sizeMPI):
		sys.stdout.flush()
		commMPI.send(0,dest=i,tag=TagEnd)

else: #I am a slave
	tag=TagRes		#Just to get into the while
	while tag!=TagEnd:
		status = MPI.Status()
		dataMS=commMPI.recv(source=0,tag=MPI.ANY_TAG,status=status) #data from Master NSend,a,b
		tag=status.Get_tag()
		if tag==TagEnd:
			sys.exit()
		#print(dataMS[1],OperSymb[tag],dataMS[2])
		#sys.stdout.flush()
		result=Operfunc[tag](dataMS[1],dataMS[2]) #fXxx(a,b)
		dataSL=[dataMS[0],result,rankMPI]	#data from slave: (i,res,rank)
		commMPI.send(dataSL,dest=0,tag=TagRes)


if rankMPI == 0:
	for i in range(ListSize):
		print(i,":",List[i][0],OperSymb[List[i][2]],List[i][1],"=",List[i][3])

sys.exit() 
