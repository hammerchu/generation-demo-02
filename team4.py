import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob 
strr = open('./news.txt', 'r').read()
def reverseWords(string):
    st = list()
 
    # Traverse given string and push all characters
    # to stack until we see a space.
    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])
 
        # When we see a space, we print
        # contents of stack.
        else:
            while len(st) > 0:
                print(st[-1], end= "")
                st.pop()
            print(end = " ")

    # Since there may not be space after
    # last word.
    while len(st) > 0:
        print(st[-1], end = "")
        st.pop()
 
# Driver Code
if __name__ == "__main__":
    string = strr
    reverseWords(string)
if __name__ == "__main__":
    print(pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)

from collections import defaultdict
vowel = defaultdict(int)

for char in text:
    vowel[char] += 1
    
print(vowel['a'])
print(vowel['e'])
print(vowel['i'])
print(vowel['o'])
print(vowel['u'])

print((vowel['a'])+(vowel['e'])+(vowel['i'])+(vowel['o'])+(vowel['u']))
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob