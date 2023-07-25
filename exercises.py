'''
Complete the following exercises with your team!
Then create a new branch with your name.
Add, commit, and push your commit to origin on this new branch.
Finally, create a pull request.
'''

def fizzbuzz():
    g = 99
    i = 0
    while i <= g:
        i += 1
        if i%3 == 0 and i%5 == 0:
            print ("FizzBuzz")
        elif i%3 == 0:
            print ("Fizz")
        elif i%5 == 0:
            print ("Buzz")
        elif i%3 != 0 or i%5 != 0:
            print (i)
    
       


#Tony
def is_palindrome(str):
    i2 = len(str) - 1
    for i in range(0, len(str)):
        print(str[i], ' ', str[i2])
        if str[i] != str[i2]:
            return False
        i2 -= 1

    return True

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if(len(str1) == len(str2)):
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        if(sorted_str1 == sorted_str2):
            return True
        else:
            return False
    else:
        return False
    


def count_vowels(str):
    '''
    Write a program that takes a string as input and counts the number of vowels
    (a, e, i, o, u, A, E, I, O, U) in the string.
    '''
    #Gunnar

    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vwlcount = 0
    for character in str:
        if character in vowels:
            vwlcount += 1
    return(vwlcount)

def reverse_list(lst):
    lst2 = lst[:]
    for i in range(0, len(lst)):
        lst[i] = lst2[len(lst2)-i-1]
    return lst

if __name__ == '__main__':
    # test and run your functions here
    print(is_palindrome('racecar'))
    fizzbuzz()
    # print(is_palindrome('not a palindrome'))
    print(is_anagram('listen', 'silent'))
    # print(is_anagram('not an anagram', 'anagram'))
    # print(count_vowels('there are vowels in HERE'))
    print(reverse_list([1, 2, 3, 4, 5]))
