"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
old_macdonald('macdonald') --> MacDonald
"""


def old_macdonald(macdonald):
    return macdonald[:3].capitalize() + macdonald[3:].capitalize()

print(old_macdonald("macdonald"))


"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""

def master_yoda(sentence):
    return "".join(sentence.split()[::-1])
    
    
print(master_yoda("I am home"))

    


