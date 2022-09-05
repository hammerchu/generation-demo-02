import random

text = './news.txt'
f = open(text, "r")
print(f.read())


f = f.replace('z', '|')
f = f.replace('y', 'z')
f = f.replace('x', 'y')
f = f.replace('w', 'x')
f = f.replace('v', 'w')
f = f.replace('u', 'v')
f = f.replace('t', 'u')
f = f.replace('s', 't')
f = f.replace('r', 's')
f = f.replace('q', 'r')
f = f.replace('p', 'q')
f = f.replace('o', 'p')
f = f.replace('n', 'o')
f = f.replace('m', 'n')
f = f.replace('l', 'm')
f = f.replace('k', 'l')
f = f.replace('j', 'k')
f = f.replace('i', 'j')
f = f.replace('h', 'i')
f = f.replace('g', 'h')
f = f.replace('f', 'g')
f = f.replace('e', 'f')
f = f.replace('d', 'e')
f = f.replace('c', 'd')
f = f.replace('b', 'c')
f = f.replace('a', 'b')
f = f.replace('|', 'a')
f = f.replace('Z', '&')
f = f.replace('Y', 'Z')
f = f.replace('X', 'Y')
f = f.replace('W', 'X')
f = f.replace('V', 'W')
f = f.replace('U', 'V')
f = f.replace('T', 'U')
f = f.replace('S', 'T')
f = f.replace('R', 'S')
f = f.replace('Q', 'R')
f = f.replace('P', 'Q')
f = f.replace('O', 'P')
f = f.replace('N', 'O')
f = f.replace('M', 'N')
f = f.replace('L', 'M')
f = f.replace('K', 'L')
f = f.replace('J', 'K')
f = f.replace('I', 'J')
f = f.replace('H', 'I')
f = f.replace('G', 'H')
f = f.replace('F', 'G')
f = f.replace('E', 'F')
f = f.replace('D', 'E')
f = f.replace('C', 'D')
f = f.replace('B', 'C')
f = f.replace('A', 'B')
f = f.replace('&', 'A')
print ("Q2 Encode:" + f)

#def pickOneMemeber():
#    '''example function'''

#    teamJDE = ['hammer', 'billy', 'chistina']
#    result = random.sample(teamJDE, 1)
#    return result


#if __name__ == "__main__":
#    print(pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
