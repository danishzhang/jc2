# 1 (a)

Jobs = [[i, j] for i in range(100) for j in range(2)]
NumberOfJobs = len(Jobs)
freepointer = -1

# 1 (b)
def Initialise():
    global NumberOfJobs
    global Jobs
    for i in range (NumberOfJobs):
        Jobs[i][0] = -1
        Jobs[i][1] = -1
        NumberOfJobs = 0
                

# 1 (c)
def AddJob(JobNum, Priority):
    global NumberOfJobs
    if NumberOfJobs == len(Jobs):
        print("Item is not added, space is full")
    else:
        Jobs[NumberOfJobs][0] = JobNum
        Jobs[NumberOfJobs][1] = Priority
        NumberOfJobs = NumberOfJobs + 1

# 1 (d)
Initialise()
AddJob(12,10)
AddJob(526,9)
AddJob(33,8)
AddJob(12,9)
AddJob(78,1)

# 1 (e) 
def InsertionSort():
    for i in range(1,len(Jobs)):
        j = i - 1
        jobNo = Jobs[i][0]
        priorityNo = Jobs[i][1]
        while (jobNo < Jobs[j][0] and priorityNo < Jobs[j][1] and j >= 0):
            Jobs[j][0], Jobs[j+1][0] = Jobs[j+1][0], Jobs[j][0]
            Jobs[j][1], Jobs[j+1][1] = Jobs[j+1][1], Jobs[j][1]
            j = j - 1 

InsertionSort()
print(Jobs)


