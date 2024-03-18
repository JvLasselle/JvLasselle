#Jared Lasselle
#JvLasselle
#Combinatorics Asgn 2

#<READ ME>
#this program will find the given rank permutation (of lex order) of the numbers in allTheNumbers where the length of the permutation is lengthOfPermutation.
#You can do whatever you want, but I only recommend modifying the three values directly below this that are maked with "#You can change this value".  Just keep the format of the list the same.
#</READ ME>

def main():
    allTheNumbers = [1,2,3,4,5,6,7,8,9,10,11,12]  #You can change this value
    rank = 999999                                     #You can change this value
    lengthOfPermutation = 12                         #You can change this value
    
    #The following triple double quotes are preventing the code inside from running.  If you would like to see what they do you may remove all of the quote marks before and after the section of code
    #Spoiler alert the code just gives all the permutations for the given set of numbers
    #If you run it, I would recommend shortening the number of possible permutations.  Because right now it takes a little while to run and keeps your computer pretty warm.
    """
    rank = 0
    while True:
        nums = []
        for i in range(len(allTheNumbers)):
            nums.append(allTheNumbers[i])
        returnedValue = lexPrint(nums, rank, lengthOfPermutation)
        if returnedValue == -1:
            break
        print(returnedValue)
        rank = rank + 1
    """ #if you take out the quotations you will get an errant -1 to appear at the end unless you also take out the line directly below this one.
    print(lexPrint(allTheNumbers, rank, lengthOfPermutation))

def lexPrint(bag, pertNum, length):
    totalPerts = factorial(len(bag)) / factorial(len(bag)-length) -1
    if pertNum > totalPerts:
        return -1
    returnMe = []
    for i in range(1, length+1):
        pertsPer = choose(len(bag)-1, length-i)
        #print(factorial(length-i+1))
        pertsPer = pertsPer * factorial(length-i)
        #print(pertsPer)
        for j in range(len(bag)):
            indexCalc = j
            if (j+1)*pertsPer > pertNum:
                break
        #print(indexCalc)
        returnMe.append(bag.pop(indexCalc))
        pertNum = pertNum - pertsPer*indexCalc
    return returnMe

def choose(n,k):
    return(factorial(n)/(factorial(k)*factorial(n-k)))

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    return fact

if __name__ == "__main__":
    main()
