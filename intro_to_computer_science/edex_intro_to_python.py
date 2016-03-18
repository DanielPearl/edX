def find_bob(s):
    """ Finds the number 'bobs' in a string
    s : string
    """
    s.lower() #set string to lowercase
    count = 0
    index = 0
    while True:
        index = s.find('bob', index)
        if index >= 0:
            count += 1
            index += 1
        else:
            return count

def recurPowerNew(base, exp):
    """
    computes baseexp by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

    returns: int or float, base^exp
    """
    if exp <= 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    else:
        return (base * recurPowerNew(base, exp - 1))

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    large = max(a,b)
    small = min(a,b)
    new_num = small

    while new_num > 1:
        if large % new_num == 0 and small % new_num == 0:
            return new_num
        else:
            new_num -= 1

    return new_num

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    count = 0
    for i in aStr:
        count += 1
    return count

def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) > 1:
        mid = len(aStr)//2
        if char == (aStr[mid]):
            return True
        elif char < (aStr[mid]):
            return search(char, aStr[:mid])
        elif char > (aStr[mid]):
            return search(num, aStr[mid:])
        else:
            return False
    else:
        return False

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False
    # Strings of different lengths won't be palindromes
    elif len(str1) != len(str2):
        return False
    # When string ends, return True
    elif str1 == "" and str2 == "":
        return True
    else:
        return str1[0] == str2[-1] and semordnilap(str1[1:-1],str2[1:-1])

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    return aTup[::2]

def plusOne(a):
    return a + 1

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest_key = None
    biggest = 0
    for key in aDict:
        if len(aDict[key]) >= biggest:
            biggest = len(aDict[key])
            biggest_key = key
        else:
            return None
    return biggest_key

def f(x):
    """
    Calculates the radioactive curve
    """
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to between start and stop times.
    """
    total_exposure = 0
    current_exposure = start #Sets current exposure equal to start of decay
    while current_exposure < stop:
        total_exposure += f(current_exposure) * step #Sets total exposure equal to sum of current_exposure
        current_exposure += step #Increments current_exposure by step amount
    return total_exposure

def FancyDivide(list_of_numbers, index):
    #define the SimpleDivide function here
    denom = list_of_numbers[index]
    try:
        return [SimpleDivide(item, denom) for item in list_of_numbers]
    except ZeroDivisionError:
        for item in range(len(list_of_numbers)):
            list_of_numbers[item] *= 0
        return list_of_numbers

def SimpleDivide(item, denom):
   return item / denom

def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"

def count_vowels(s):
    a = s.count('a')
    e = s.count('e')
    i = s.count('i')
    o = s.count('o')
    u = s.count('u')
    vowels = a + e + i + o + u
    return vowels

def is_palindrome(aString):
    '''
    aString: a string
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ""
    n = 0
    reversed_string = ""
    for letter in aString:
        if letter in alphabet:
            new_string += letter
    for letter in range(len(new_string),0,-1):
        reversed_string += new_string[letter-1]
    if reversed_string == new_string:
        return True
    return False

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    total = 0
    for i in range(len(listA)):
        total += (listA[i] * listB[i])
    return total

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    new_list = [] #initializes new list
    for i in aList:
        if type(i) == list:
            new_list.extend(flatten(i)) #extends i recursively
        else:
            new_list.append(i) #appends i to new_list
    return new_list #returns new list

def f(i1, i2):
    return i1 + i2

def dict_interdiff(d1, d2):
    inter_dict = {} #initiate intersect dictionary
    diff_dict = {} #initiate difference dictionary

    for key in d1.keys():
        if key in d2.keys(): #if d1 and d2 contain the same keys
            inter_dict[key] = f(d1[key],d2[key]) #add keys to inter_dict
        else:
            diff_dict[key] = d1[key] #add d1 keys to diff_dict
    for key in d2.keys():
        if key not in d1.keys(): #if d1 and d2 do not contain the same keys
            diff_dict[key] = d2[key] #add d2 keys to diff_dict

    return (inter_dict, diff_dict) #return dictionary tuple

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    new_list = []
    for s in L:
        if f(s):
            new_list.append(s)
    L[:] = new_list
    return len(L)

def lenRecur(s):
   if s == '':
      return 0
   else:
      return 1 + lenRecur(s[1:])

def modSwapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L

import random

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3

        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1

        for i in range(numVowels, self.HAND_SIZE):
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1

    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans

    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    new_dict = {} #initializes empty dict
    unique_list = [] #initializes empty list of unique keys
    key_list = [] #initializes empty list of repetitive keys

    for key in d:
        key_list.append(key)
        if d[key] not in unique_list: #if value is not a repeat
            unique_list.append(d[key])
            new_dict[d[key]] = key_list
        else: #if value is a repeat
            new_dict[d[key]] += key_list
        new_dict[d[key]].sort() #sorts list for each key
        key_list = [] #clears list
    return new_dict

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4

def getSublists(L, n):
    """
    Returns a list of all possible sublists in L of length n without skipping elements in L.

    L:list
    n:int
    """
    full_list = [] #initializes full_list
    sub_list = [] #initializes sub_list
    start = 0 #initialized start value
    end = start + n #initialized end value

    for i in range(len(L)):
        if len(L[start:end]) >= n: #if length of slice is >= int n
            sub_list += (L[start:end]) #append slice to sub_list
            start += 1 #increment start value in slice
            end += 1 #increment end value in slice
            full_list.append(sub_list) #append sublist to returned list
            sub_list = [] #clear sublist
    return full_list

def longestRun(L):
    best_list = []
    sub_list = []
    previous = None

    for i in L:
        if i >= previous and previous != None:
            if len(sub_list) <= 0:
                sub_list.append(previous)
            sub_list.append(i)
        else:
            sub_list = [i]
        if len(sub_list) > len(best_list):
            best_list = sub_list
        previous = i
    return len(best_list)

## DO NOT MODIFY THE IMPLEMENTATION OF THE Person CLASS ##
class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name

class USResident(Person):
    """
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status == "citizen" or status == "legal_resident" or status == "illegal_resident":
            self.status = status
        else:
            raise ValueError

    def getStatus(self):
        """
        Returns the status
        """
        return self.status

#------------------------------------------------------------------------------#

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return "Prof. {0} says: {1}".format(self.name, self.lecture(stuff))

class ArrogantProfessor(Professor):
    def say(self, stuff):
        return ("{0} says: It is obvious that I believe that {1} says: {2}".format(self.name, self.name, stuff))
    def lecture(self, stuff):
        return ("It is obvious that I believe that {0} says: {1}").format(self.name, stuff)
