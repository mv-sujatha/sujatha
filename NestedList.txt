def nested_list(num,names_list,scores_list):
    result=[]
    for i in range(len(names_list)):
        if names_list[i][1]==second_lowest:
            result.append(names_list[i][0])
    result.sort()
    print('\n'.join(result))
num=int(input("enter any number"))
names_list=[]
scores_list=[]
for i in range(num):
    names=input("enter any name")
    scores=float(input("enter any score"))
    names_list.append([names,scores])
    scores_list.append(scores)
sorted1=sorted([*set(scores_list)])
second_lowest=sorted1[1]
nested_list(num,names_list,scores_list)
                                        

