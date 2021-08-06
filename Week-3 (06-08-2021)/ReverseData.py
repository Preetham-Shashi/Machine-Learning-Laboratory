#221910301050

def reverse_file(filename):
    S=ArrayStack()
    original=open(filename)
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()
        
    output=open("newfile",'w') #enter file name to store new contents here
    while not S.is_empty():
        output.write(S.pop()+'\n')
    output.close()
reverse_file("file") #existing file name here