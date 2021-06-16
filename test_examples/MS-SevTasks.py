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

ListSize=10	#size of the list.
if ListSize<sizeMPI-1:
	if rankMPI==0:
		print("List size < #slaves") #just the master print
	sys.exit() #all processes do the exit

TagAdd=0
TagSub=1
TagMul=2
TagDiv=3
TagResult=4
TagEnd=5
OperNumb=[TagAdd,TagSub,TagMul,TagDiv]
Operfunc={TagAdd:fAdd, TagSub:fSub, TagMul:fMul, TagDiv:fDiv}
OperSymb={TagAdd:"+", TagSub:"-", TagMul:"*", TagDiv:"/"}


if rankMPI == 0: 	#I am master
	List=[]

	for i in range (ListSize):
		List.append([i,i+1,random.choice(OperNumb),None]) #a,b,oper,res	

	#Feed slaves 
	for i in range(0,sizeMPI-1):
		dataMS=[i,List[i][0],List[i][1]]
		commMPI.send(dataMS,dest=i+1,tag=List[i][2])

	#receive from slaves and feed again
	for i in range(sizeMPI-1,ListSize):
		dataSL=commMPI.recv(source=MPI.ANY_SOURCE,tag=TagResult)
		List[dataSL[0]][3]=dataSL[1]
		dataMS=[i,List[i][0],List[i][1]]
		commMPI.send(dataMS,dest=dataSL[2],tag=List[i][2])

 	#receive from pending slaves: all slaves have send back and sent terminate 
	for i in range(0,sizeMPI-1):       		
		dataSL=commMPI.recv(source=MPI.ANY_SOURCE,tag=TagResult)
		List[data[0]][3]=data[1]	
		#send exit message to all workers
		commMPI.send(0,dest=dataSL[2],tag=List[i][2])
	

else: #I am a slave
	status = MPI.Status()
	dataMS=commMPI.recv(source=0,tag=MPI.ANY_TAG,status=status)
	tag=status.Get_tag()
	if tag==TagEnd:
		sys.exit()
	result=Operfunc[tag](dataMS[1],dataMS[2]) #fXxx(a,b)
	print(dataMS[1],OperSymb[tag],dataMS[2],"=",result)
	dataSL=[dataMS[0],result,rankMPI]
	commMPI.send(dataSL,dest=0,tag=TagResult)


if rankMPI == 0:
	for i in rangue(ListSize):
		print(List[1],OperSymb[List[3]],List[2],"=",List[4])

sys.exit() 
