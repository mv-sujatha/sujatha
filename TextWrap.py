import textwrap
def wrap(string,maxwidth):
    l=textwrap.wrap(string,maxwidth)
    s='\n'.join(l)
    print(s)
string=input("enter any string")
maxwidth=int(input("enter maximum width"))
wrap(string,maxwidth)
