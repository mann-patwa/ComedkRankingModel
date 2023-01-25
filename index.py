from random import *

class Student():
    def __init__(self,id,rank,alloted,preferences = []):
        self.id = id
        self.rank = rank
        self.alloted = alloted
        self.preferences = preferences
    def __str__(self):
        print(f"id:{self.id}")
        print(f"rank:{self.rank}")
        print("preferences:")
        for preference in self.preferences:
            print(f"{preference}")
        print(f"alloted:{self.alloted}")
        return ''

class College():
    # branches is an object that has
    def __init__(self,id,branches):
        self.branches = branches
        self.id = id

def makeStudents(numOfStudents):
    # creating a list to assign ranks
    ranklist= []
    for i in range (1,numOfStudents+1):
        ranklist.append(i)
    shuffle(ranklist)
    student_list = []
    for i in range(numOfStudents):
        x = randint(0,(len(branch_list)-1))
        y = randint(0,(len(branch_list)-1))
        z = randint(0,(len(branch_list)-1))

        student = Student(i+1,ranklist[i],{},[
            {"collegeId" : (randint(1,numOfColleges)),"branch" : branch_list[x] },
            {"collegeId" : (randint(1,numOfColleges)),"branch" : branch_list[y] },
            {"collegeId" : (randint(1,numOfColleges)),"branch" : branch_list[z] }])
        student_list.append(student)
    return student_list
def makeColleges(numOfColleges,noOfSeats):

    college_list = []
    for i in range(1,numOfColleges+1):
        newCollege = College(i,{
            "cs":noOfSeats,
            "is" : noOfSeats,
            "ec":noOfSeats
            })
        college_list.append(newCollege)
    return college_list

numOfColleges = 2
numOfStudents = 20
numOfSeats = 2
branch_list  = ["cs",'ec',"is"]
studentList = makeStudents(numOfStudents)
collegeList = makeColleges(numOfColleges,numOfSeats)
studentList.sort(key=lambda x: x.rank)
for student in studentList:
    preferences = student.preferences
    for preference in preferences:
        selected_college = collegeList[(preference["collegeId"]-1)]
        selected_branch  = preference["branch"]
        if ((selected_college.branches)[selected_branch] > 0):
            student.alloted = {"College Id":preference['collegeId'], "branch": selected_branch}
            selected_college.branches[selected_branch] -=1
            break
for i in studentList:
    print(i)

