def string_split_join(string):
    string1=string.split()
    string2='-'.join(string1)
    return string2
stg=input("enter any string")
print(string_split_join(stg))
