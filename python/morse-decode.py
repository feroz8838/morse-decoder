import sys 
data={ 
    # Letters
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",

    # Numbers
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    # Common punctuation
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-"
    }

def get_inp():
    if len(sys.argv)==1:
        return input("Enter the string to decode:")
    else:
        return sys.argv[1]
        
inp=str(get_inp())
print("Entered string: ",inp)
inp=inp.upper()
decd=str()
for i in inp:
    decd+=(data[i]+' ')
    
print("Decoded string: ",decd)