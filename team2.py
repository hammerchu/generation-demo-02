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
text = './news.txt'
f = open(text, "r")
print("a = ", f.read().count("a"))
text = './news.txt'
f = open(text, "r")
print("e = ", f.read().count("e"))
text = './news.txt'
f = open(text, "r")
print("i = ", f.read().count("i"))
text = './news.txt'
f = open(text, "r")
print("o = ", f.read().count("o"))
text = './news.txt'
f = open(text, "r")
print("u = ", f.read().count("u"))

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
