from __future__ import print_function
updatedSpaces=['-','-','-','-','-']
word='steve'
lives=5
updatedSpaces= []

def initialize():
    global word
    global updatedSpaces
    word = "airport"
    print("_ " * len(word))
    updatedSpaces = ("_ " * len(word))
    print("Try to guess the word within 6 tries")
    print(updatedSpaces)
    
def getLetter():
    global letter
    print("What is your guess?")
    letter = raw_input()
   
def check(letter):
    global lives
    global updatedSpaces
    global word
    if letter in word:
        for i in range(0,len(word)-1):
            Hamza=word.find(letter, i, len(word))
            if Hamza != -1:
                updatedSpaces[Hamza]=letter
    else:
        lives=lives-1
        print('Not in word,', lives, 'lives left!')
    print(updatedSpaces)
     
def won():
    global lives
    if updatedSpaces == word:
        print('Congratulations, you got the word!')
    else:
        '''lives = lives -1
        if lives == 0:
            print('You lost :(')'''
        getLetter()

def main():
    initialize()
    getLetter()
    #check()
    

        
        
        
        
    
        
        
    

        
