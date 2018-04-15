s = 'superconductivity'
i = 0
i = 0 
#while i < len(s):
#    print (s[i])
#    i = i + 1

#t = ''
#while i < len(s):
#    if i < (len(s) - 1):
#       t = t + s[i] + ' ' + ','
#    else:
#        t = t + s[i]
#    i = i + 1
#print (t)

t = ''
while i < len(s):
    t = t + s[i] + ' ' + ','
    i = i + 1
print (t)

def reform(string):
    t = ''
    i = 0
    while i < len(string):
        if i < (len(string) - 1):
           t = t + string[i] + ' ' + ','
        else:
            t = t + string[i]
        i = i + 1
    print (t)
