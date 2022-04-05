#Practice slide 
def find_last(s, sub):
    # default condition
    if(len(sub) > len(s) or ((s.find(sub)) == -1)):
        return None
    currentIndex = s.find(sub)
    while(True):
        index = s.find(sub, currentIndex + len(sub))
        if(index == -1):
            break
        else:
            currentIndex = index
    return currentIndex
print(find_last("testnowtest", "test"))

while True:    
    try: 
        if find_last i  

#print(find_last("testnowtest", "test"))