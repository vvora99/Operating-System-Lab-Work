n=int(input("Enter Number of processes"))

at=[]
bt=[]
for i in range(n):
    at.append(int(input("Enter AT of process "+str(i+1)+" : ")))
    bt.append(int(input("Enter BT of process "+str(i+1)+" : ")))

tq=int(input("Time quantum : "))

tempat=[]
for a in at:
    tempat.append(a)

tempbt=[]
for b in bt:
    tempbt.append(b)

chk=[]
for i in range(n):
    chk.append(0)

schedule_array=[]       #[process, start, end]
queue=[]

minat=min(at)
indat=at.index(minat)
queue.append(indat+1)

for i in range(60):
    incomp=0
    temp=[]
    indat=queue[0]-1
    temp.append(indat+1)
    chk[indat]=1
    if len(schedule_array)==0:
        temp.append(at[indat])
    else:
        if at[indat]>=schedule_array[len(schedule_array)-1][2]:
            temp.append(at[indat])
        else:
            temp.append(schedule_array[len(schedule_array)-1][2])
    if bt[indat]<=tq and bt[indat]>0:
        c1=temp[len(temp)-1]+bt[indat]
        temp.append(c1)
        bt[indat]=0
    else:
        c1=temp[len(temp)-1]+tq
        temp.append(c1)
        bt[indat]=bt[indat]-tq
        if bt[indat]!=0:
            incomp=1
    queue.remove(indat+1)
    for i in range(n):
        if chk[i]==0 and at[i]<=c1 and bt[i]>0 and (i+1) not in queue:
            queue.append(i+1)
    if incomp==1:
        queue.append(indat+1)
    schedule_array.append(temp)
    if len(queue)==0:
        break
print("Scheduled process array : [processid,start,end] ")
print(schedule_array)

ct=[]
for i in range(1,n+1,1):
    t=[]
    for arr in schedule_array:
        if arr[0]==i:
            t.append(arr[2])
    ct.append(max(t))
        
print("CT : ",ct)

tat=[]
for i in range(n):
    tat.append(ct[i]-tempat[i])
print("TAT : ",tat)

wt=[]
for i in range(n):
    wt.append(tat[i]-tempbt[i])
print("WT : ",wt)

rt=[]
for i in range(n):
    if schedule_array[i][1]==0:
        rt.append(0)
    else:
        rt.append(ct[i-1]-tempat[i])
print("RT : ",rt)

avgtat=sum(tat)/n
avgwt=sum(wt)/n
throughput=float(n)/ct[len(ct)-1]
print("Average TAT : ",avgtat)
print("Average WT : ",avgwt)
print("Throughput",throughput)
