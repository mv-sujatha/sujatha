def count_substring(string,sub_string):
    substring_len=len(sub_string)
    c=0
    for i in range(len(string)):
        if string[i:substring_len+i]==sub_string:
            c=c+1
    return c
