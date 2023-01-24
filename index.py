from random import *
numOfColleges = 1
numOfStudents = 10
branch_list  = ["cs",'ec',"is"]
class Student():
    def __init__(self,id,rank,alloted,preferences = []):
        self.id = id
        self.rank = rank
        self.alloted = alloted
        self.preferences = preferences
class College():
    # branches is an object that has
    def __init__(self,id,branches):
        self.branches = branches
        self.id = id

def makeStudents(numOfStudents):
    # creating a list to assign ranks
    student_list = []
    for i in range(numOfStudents):
        x = randint(0,(len(branch_list)-1))
        y = randint(0,(len(branch_list)-1))
        z = randint(0,(len(branch_list)-1))

        student = Student(i+1,(randint(1,numOfStudents)),{},[
            {"collegeId" : (randint(1,numOfColleges)),"branch" : branch_list[x] },
            {"collegeId" : (randint(1,numOfColleges)),"branch" : branch_list[y] },
            {"collegeId" : (randint(1,numOfColleges)),"branch" : branch_list[z] }])
        student_list.append(student)
    return student_list
def makeColleges(numOfColleges):
    college_list = []
    for i in range(1,numOfColleges+1):
        newCollege = College(i,{
            "cs":{"name": "cs", "seats": 1},
            "is" : {"name": "is","seats":1},
            "ec":{"name": "ec","seats":1}
            })
        college_list.append(newCollege)
    return college_list


studentList = makeStudents(numOfStudents)
collegeList = makeColleges(numOfColleges)
# print((studentList[0].preferences[0])['branch'])
for student in studentList:
    preferences = student.preferences
    for preference in preferences:
        selected_college = collegeList[(preference["collegeId"]-1)]
        selected_branch  = preference["branch"]
        if ((selected_college.branches)[selected_branch]["seats"] > 0):
            student.alloted = {"College Id":preference['collegeId'], "branch": selected_branch}
            selected_college.branches[selected_branch]['seats'] -=1
            break
for i in studentList:
    print(i.preferences)
    print(i.alloted)