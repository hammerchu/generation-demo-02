import random

text = './news.txt'
f = open(text, "r")
print(f.read())


def pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result

# Task-4

# opening the file in read mode
textfile = open("/content/sample_data/news.txt")
with open("textfile","r") as fp:
  contents = fp.read().split()

# reversing each word(element) of the list
for number in range(len(contents)):
  contents[number] = contents[number][::-1]

#creating a sting from the list
contents = (" ").join(contents)

# opening the file in write mode and write the content
with open("textfile", "w") as fp:
  fp.write(contents)






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