n=int(input("Enter Number of processes"))

at=[]
bt=[]
for i in range(n):
    at.append(int(input("Enter AT of process "+str(i+1)+" : ")))
    bt.append(int(input("Enter BT of process "+str(i+1)+" : ")))

tempat=[]
for a in at:
    tempat.append(a)

tempbt=[]
for b in bt:
    tempbt.append(b)

schedule_array=[]       #[process, start, end]

count=0
for c in range(50):
    temp=[]
    if len(schedule_array)==0:
        minat=min(at)
        indat=at.index(minat)
        temp.append(indat+1)
        temp.append(at[indat])
        temp.append(at[indat]+1)
        bt[indat]=bt[indat]-1
        if bt[indat]==0:
            count=count+1
    else:
        tct=schedule_array[len(schedule_array)-1][2]
        tbt=[]
        for a in range(len(at)):
            if at[a]<=tct and bt[a]>0:
                tbt.append(bt[a])
        if len(tbt)==0:
            count=count+1
            break
        mintbt=min(tbt)
        indat=bt.index(mintbt)
        temp.append(indat+1)
        if at[indat]>=schedule_array[len(schedule_array)-1][2]:
            temp.append(at[indat])
        else:
            temp.append(schedule_array[len(schedule_array)-1][2])
        temp.append(temp[len(temp)-1]+1)
        bt[indat]=bt[indat]-1
    schedule_array.append(temp)
    if count==n:
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
