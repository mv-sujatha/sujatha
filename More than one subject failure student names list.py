def more_than_one_sub(array, pass_mark):
    students = []
    for obj in array:
        [name, marks] = list(obj.values())
        count = 0
        for mark in marks:
            if mark < pass_mark:
                count += 1
                if count > 1:
                    students.append(name)
                    break
                
    print (*students, sep = "\n")
arr = [
    {
        'name': 'sujatha',
        'marks': [10,20,30,40,50,60]
    },
    {
        'name': 'jagam',
        'marks': [10,20,30,70,80,90]
    },
        {
        'name': 'naga',
        'marks': [30,40,50,60,70,80]
    },
    {
        'name': 'madhavi',
        'marks': [50,60,70,80,90,10]
    },
        {
        'name': 'divya',
        'marks': [70,89,69,39,20,60]
    },
    {
        'name': 'uma',
        'marks': [60,70,80,90,40,50]
    },
]

pm = 25

more_than_one_sub(arr, pm)
