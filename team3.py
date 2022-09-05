import random

text = './news.txt'
f = open(text, "r")
#print(f.read())

def taskThree():
para=f.read()
line1='Beef brisket noodles is a famous dish in Hong Kong.'[::-1]
line2='It is something that tourists (back when we had tourists) would seek out, and locals argue about which place makes the best version, and which cuts of beef they prefer, because these shops sell more than just brisket.'[::-1]
line3='In addition to beef in a light broth, they also offer curried beef or tendon, which makes for a nice change.'[::-1]
line4='For braised dishes, I normally use brisket, but the quality of the dish depends on which part of the brisket you get.'[::-1]
line5="The thick, fatty, layered part of the brisket is tender when it’s cooked low-and-slow, but if you use the flat, lean part, the meat becomes hard and dry."[::-1]
line6="So lately, I’ve been using beef cheek, which gives more consistent results."[::-1]
line7="If I’m not in a rush, I cook the ingredients in a clay pot placed over a low flame – it usually takes about five hours, if you're using tendon."[::-1]

result=f'{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}'
return result

print(taskThree)
#def pickOneMemeber():
    #'''example function'''

    #teamJDE = ['hammer', 'billy', 'chistina']
    #result = random.sample(teamJDE, 1)
    #return result


if __name__ == "__main__":
    #print(pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
    
    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I

    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob