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


message = 'Beef brisket noodles is a famous dish in Hong Kong. It is something that tourists back when we had tourists would seek out, and locals argue about which place makes the best version, and which cuts of beef they prefer, because these shops sell more than just brisket. In addition to beef in a light broth, they also offer curried beef or tendon, which makes for a nice change. For braised dishes, I normally use brisket, but the quality of the dish depends on which part of the brisket you get. The thick, fatty, layered part of the brisket is tender when it\’s cooked low-and-slow, but if you use the flat, lean part, the meat becomes hard and dry. So lately, I\’ve been using beef cheek, which gives more consistent results. If I\’m not in a rush, I cook the ingredients in a clay pot placed over a low flame – it usually takes about five hours, if you\'re using tendon. If I need the dish to be ready in about one-third or less of that time, I use a pressure cooker – either a stovetop version which is more powerful or an electric model an Instant Pot or something similar, which takes a little longer.'

a = message.count('a')
e = message.count('e')
i = message.count('i')
o = message.count('o')
u = message.count('u')

print(a)
print(e)
print(a+e+i+o+u)

    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
