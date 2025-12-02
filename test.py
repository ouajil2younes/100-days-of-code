n=["4.0O0",
"-1.00",
"+4.54",
"SomeRandomStuff"]

variable=[]
test=[]
for  j in n:
        for element in j:
            if 'a' <= element <= 'z' or 'A' <= element <= 'Z':
                variable.append('False')
                test.append(element)
        else:
            variable.append('true')      
        if j[0:2]=='+-' or j[0:2]=='-+':
            variable.append('False')
            test.append(j[0:2])
        if j.count('.')>=2:
            variable.append('False')
        if j[::1]=='.':
            test.append(j[::1])
            variable.append('False')        
        if 'False' in variable:
            print(False)
            variable.clear()
        else:
            print(True)

        