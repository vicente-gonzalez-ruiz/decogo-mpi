from mpi4py import MPI
import random

def fAdd(a,b):
	return a+b

def fSub(a,b):
	return a-b

def fMul(a,b):
	return a*b
 
def fDiv(a,b):
	return a/b


comm = MPI.COMM_WORLD
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()
size = MPI.COMM_WORLD.Get_size()

TagAdd=0
TagSub=1
TagMul=2
TagDiv=3
OperNumb=[TagAdd,TagSub,TagMul,TagDiv]
Operfunc={TagAdd:fAdd, TagSub:fSub, TagMul:fMul, TagDiv:fDiv}
OperSymb={TagAdd:"+", TagSub:"-", TagMul:"*", TagDiv:"/"}


if rank == 0: 	#I am master
	ListSize=1000	#size of the list.
	List=[]

	for i in range (ListSize):
		List.append([i,i+1,random.choice(OperNumb),None]) #a,b,oper,res	

	for i in range(0,size-1):
		data=[List[i][0],List[i][1]]
		print(List[i][2])
		comm.send(data,dest=i+1,tag=List[i][2])

else: #I am a slave
	status = MPI.Status()
	data=comm.recv(source=0,tag=MPI.ANY_TAG,status=status)
	tag=status.Get_tag()
	result=Operfunc[tag](data[0],data[1]) #fXxx(a,b)
	print(data[0],OperSymb[tag],data[1],"=",result) 
