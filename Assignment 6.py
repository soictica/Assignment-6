print("Question 1\n")
lower = int(input("Please input a lower bound\n"))

upper = int(input("Please input an upper bound\n"))

step = int(input("Please input a step size\n"))

numlist = []

if step > 0:
    for i in range(lower, upper+1, step):
        numlist.append(i)
        
else:
    for i in range(lower, upper-1, step):
        numlist.append(i)     

numlist = sorted(numlist)

print(numlist)
#try:
themean = sum(numlist)/len(numlist)
print(f"Mean equals {themean}")

themedian = 0
try:
#if (len(numlist)-1)/2 % 0:
    if (len(numlist)-1) % 2 == 0:
        themedian = numlist[int((len(numlist)-1)/2)]
 
    elif len(numlist) == 2:
        themedian = (sum(numlist)/2)    

    else:
        index = (len(numlist) - 2) / 2
        themedian = (numlist[int((len(numlist)-2)/2)] + numlist[int(((len(numlist)-2)/2)+1)])/2
    #themedian = (numlist[index] + numlist[index+1])/2

    print(f"Median equals {themedian}")

    therange = max(numlist) - min(numlist)
    print(f"Range equals {therange}")
    
except:
    print("Please enter a valid input")
    
#Q2   
print("\nQuestion 2")
def Convert(string):
    li = list(string.split(" "))
    #for thisnum in li:
    #    thisnum = int(thisnum)
    return li

message = input("Enter your code\n")

try:
    message = str(message)

    messsagelist = []
    messagelist = (Convert(message))

    #print(message)
    #print(messagelist)

    for i in messagelist:
        thisnum = int(i)
        if thisnum>0:
            thisoct = oct(thisnum)
            thisasc = ascii(thisoct)
            print(thisasc)
        
        else:
            print(thisnum)

except:
    print("Please enter a valid input")



