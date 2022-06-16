import turtle
import matplotlib
import random
matplotlib.use('Agg')

value_body = 1
###############################################################################
#Function that create a dictionary with the secret word
def hangman_words():
    secret_word = {
        1: 'elefante',
        2: 'avion',
        3: 'pais',
        4: 'programacion',
        5: 'empresa',
        6: 'amistad',
        7: 'submarino',
        8: 'deuda',
        9: 'payaso',
        10: 'idioma'
    }
    return secret_word


###############################################################################
#Function that allows to select a letter of the secret word

def select_letter(value_body):
    secret_word = hangman_words()
    random_number = random.randint(1,10)
    secret_word = secret_word[random_number]
    print(secret_word)
    secret_word_len = len(secret_word)
    #print(str(secret_word_len))
    secret_word_encrypted = '*' * secret_word_len
    print(secret_word_encrypted)

    while secret_word_len > 0:
        letter = input('Por favor ingrese una letra: ')
        lst = []

        for pos, char in enumerate(secret_word):
            if(char == letter):
                lst.append(pos)

        #print(lst)
        lst_len = len(lst)
        #print('Cantidad letras ' + str(lst_len))

        if len(lst) > 0:
            print('La letra existe')
            for i in lst:
                secret_word_encrypted = secret_word_encrypted[:i] + letter + secret_word_encrypted[i+1:]
        
            print(secret_word_encrypted)
            secret_word_len = secret_word_len - lst_len
            if secret_word_len == 0:
                print('Ganaste!!!')
        else:
            print('La letra no existe')
            print(secret_word_encrypted)
            draw_hangman(value_body)
            value_body = value_body + 1
            if value_body >= 9:
                print('Perdiste!!')
                break
            else:
                pass    
            

###############################################################################
#Function that allows to draw a hangman

def draw_hangman(part_Body):

    if part_Body == 1: 
        turtle.circle(50)
        return 2
        # A head is drawing
    elif part_Body == 2:  
        turtle.goto(0,0)
        turtle.right(90)
        turtle.forward(150)
        return 3
        # The body is drawing
    elif part_Body == 3:
        turtle.up()
        turtle.goto(0,-150)
        turtle.down()
        turtle.right(-150)
        turtle.forward(-100)
        return 4
        # The right leg is drawing
    elif part_Body == 4:
        turtle.up()
        turtle.goto(0,-150)
        turtle.down()
        turtle.right(-240)
        turtle.forward(100)
        return 5
        # The left leg is drawing
    elif part_Body == 5:
        turtle.up()
        turtle.goto(0,-75)
        turtle.down()
        turtle.left(100)
        #turtle.left(130)
        turtle.forward(100)
        return 6
        # The left arm is drawing
    elif part_Body == 6:
        turtle.up()
        turtle.goto(0,-75)
        turtle.down()
        turtle.right(260)
        #turtle.left(65)
        turtle.forward(100)
        return 7
        # The right arm is drawing
    elif part_Body == 7:
        turtle.up()
        turtle.goto(-15,50)
        turtle.down()
        turtle.left(10)
        turtle.forward(20)
        turtle.up()
        turtle.goto(-23,56)
        turtle.down()
        turtle.right(90)
        turtle.forward(10)
        turtle.left(-180)
        turtle.forward(20)
        return 8
        # The left eye is drawing
    elif part_Body == 8:
        turtle.up()
        turtle.goto(15,50)
        turtle.down()
        turtle.left(-180)
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(20)
        turtle.up()
        turtle.goto(15,50)
        turtle.down()
        turtle.left(-90)
        turtle.forward(10)
        turtle.left(180)
        turtle.forward(20)
        return 9
        # The right eye is drawing
    turtle.done()
    

###############################################################################
#Run function
def run():
    select_letter(value_body)

if __name__== '__main__':
    run()