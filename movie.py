def bollywood():
    if a=='F' or a=='f':
        print("Andaz Apna Apna")
        print("Gol Maal")
        print("Chupke Chupke")
        print("Munna Bhai")
        print("Hera Pheri")
        print("3 Idiots")
        print("Vicky Donor")
        print("Delhi Belly")
    elif a=='H' or a=='h':
        print('Bhoot – Part One: The Haunted Ship')
        print('Laxmii')
        print('Stree')
        print('Roohi')
        print('Phillauri')
    elif a=='e' or a=='E':
        print('TAARE ZAMEEN PAR')
        print('THE SKY IS PINK')
        print('KAL HO NAA HO')
        print('WE ARE FAMILY')
        print('URI')
        print('PINK')
    else:
        print('Invalid choise pls try again!!')
def hollywood():
    if a=='F' or a=='f':
        print('The Hangover')
        print('Bad Teaher')
        print('Due Date')
        print('Yes, God, Yes')
        print('The Dictator')
    elif a=='e' or a=='E':
        print('A Star is Born')
        print('Love Simon')
        print('Romeo + Juliet')
        print('La La Land')
        print('A Walk to Remember')
    elif a=='H' or a=='h':
        print('The Nun')
        print("Don't Breathe")
        print('Insidious')
        print('The Conjuring')
        print('A Quiet Place')
    else:
        print('Invalid choise pls try again!!')
print("F for Funny")
print("H for Horror")
print("E for Emotional")
a=input("Enter ur mood:")
print("B for Bollywood")
print("H for Hollywood")
b=input("Enter ur choice")
if b=='B' or b=='b':
    bollywood()
elif b=='h' or b=='H':
    hollywood()
else:
    print('Invalid choise pls try again!!')
