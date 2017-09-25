

def alphabet_position(letter):
    alph_lower = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    alph_upper ={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

    for char in letter:
        for k, v in alph_lower.items():
            if char == k:
                return  v
            else:
                for k, v in alph_upper.items():
                    if char == k:
                        return  v
        #else:
            #return char


def rotate_character(char, rot):
    alph_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alph_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter_value = alphabet_position(char)
    
    if char not in alph_lower and char not in alph_upper:
        return char
    else:
        for k in alph_lower:
            if char == k:
                if int(letter_value) + int(rot) <= 25: 
                    new_letter = alph_lower[int(letter_value) + int(rot)]
                else:
                    new_letter = alph_lower[(int(letter_value) + int(rot))%26]
            else:
                for k in alph_upper:
                    if char == k:
                        if int(letter_value) + int(rot) <= 25:
                            new_letter = alph_upper[int(letter_value) + int(rot)]
                        else:
                            new_letter = alph_upper[(int(letter_value) + int(rot))%26]
        return new_letter

def rotate_string(text, rot):
    new_message = ''
    for char in text:
        letter = rotate_character(char, rot)
        new_message = new_message + letter

    return new_message