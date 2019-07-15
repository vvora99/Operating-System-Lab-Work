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

for c in range(n):
    temp=[]
    if len(schedule_array)==0:
        minat=min(at)
        indat=at.index(minat)
        tbt=[]
        for i in range(len(at)):
            if at[i]==minat:
                tbt.append(bt[i])
        mintbt=min(tbt)
        indtbt=bt.index(mintbt)
        temp.append(indtbt+1)
        temp.append(at[indtbt])
        temp.append(at[indtbt]+bt[indtbt])
        at[indtbt]=1000
        bt[indtbt]=1000
    else:
        minat=min(at)
        indat=at.index(minat)
        if minat>=schedule_array[c-1][2]:
            tbt=[]
            for i in range(len(at)):
                if at[i]==minat:
                    tbt.append(bt[i])
            mintbt=min(tbt)
            indtbt=bt.index(mintbt)
            temp.append(indtbt+1)
            temp.append(at[indtbt])
            temp.append(at[indtbt]+bt[indtbt])
            at[indtbt]=1000
            bt[indtbt]=1000
        else:
            tbt=[]
            for i in range(len(at)):
                if at[i]<=schedule_array[c-1][2]:
                    tbt.append(bt[i])
            mintbt=min(tbt)
            indtbt=bt.index(mintbt)
            temp.append(indtbt+1)
            temp.append(schedule_array[c-1][2])
            temp.append(schedule_array[c-1][2]+bt[indtbt])
            at[indtbt]=1000
            bt[indtbt]=1000
    schedule_array.append(temp)
print("Scheduled process array : [processid,start,end] ")
print(schedule_array)

ct=[]
schedule_array.sort()
for arr in schedule_array:
    ct.append(arr[2])
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
