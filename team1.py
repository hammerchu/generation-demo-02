import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result


if __name__ == "__main__":
    print(pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
def reverseWords(string):
    st = list()

    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])

        else:
            while len(st) > 0:
                print(st[-1], end= "")
                st.pop()
            print(end = " ")

    while len(st) > 0:
        print(st[-1], end = "")
        st.pop()

if __name__ == "__main__":
    string = f
    reverseWords(string)