def find_avg():
    n=int(input("enter any number"))
    student_marks={}
    for i in range(n):
        names,*marks=input("enter name and scores with spaces").split()
        scores=list(map(int,marks))
        student_marks[names]=scores
    query_name=input("enter any name from the dictionary")
    total_marks=(sum(student_marks[query_name])/len(scores))
    average="{:.2f}".format(total_marks)
    print(average)
find_avg()
