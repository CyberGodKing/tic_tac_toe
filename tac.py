import os , sys , random , time 

total_plays=[ ]
position = [1,2,3,4,5,6,7,8,9]
ai_choice= [1,2,3,4,5,6,7,8,9] 

def board():
    print('___________________\n| ',position[0],' | ',position[1],' | ',position[2],' |\n___________________\n| ',position[3],' | ',position[4],' | ',position[5],' |\n___________________\n| ',position[6],' | ',position[7],' | ',position[8],' |\n___________________')
 
def menu():
     option() 
     os.system("clear||cls")
 
 
def option():
    while True:
        try:
            print(' ENTER GAME MODE  ::   ')
            mode=int(input('\n1 . SINGLE PLAYER \n2 . MULTIPLE PLAYERS  \n3. HELP \n4 . ABOUT  \n5 , EXIT \n -------- '))
            if mode == 5 :
                print('\nTHANK YOU FOR TRYING OUT OUR GAME ')
                time.sleep(2)
                os.system('clear')
                break 
               
            elif mode == 4 :
                print('\n WELCOME TO PYTHON COMMAND LINE TIC-TAC-TOE \nthis game was built to illustrate the python CLI ability,  kindly follow us at for more Python CLI codes')
                time.sleep(10)
                os.system('clear')
            elif mode == 3 :
                    print(' \n ----Help \n kindly select your symbol \nthen choose where to place them by entering the number in the index position you want to play')
                    time.sleep(10)
                    os.system('clear')
            elif mode==1:
                os.system('clear')
                single_player()
        except ValueError:
            os.system("clear||cls")
    
        


def single_player():
    board()
    symbol= str(input('\nCHOOSE YOUR SYMBOL   [[[[     X   --or--   O    ]]]]    -|-|-|   '))
    while True:
        try:
                #while True:
                
                allowed=['X' , 'O']
                if symbol != allowed[0] and symbol != allowed[1] and symbol != allowed[0].lower() and symbol != allowed[1].lower():
                    print("\n INVALID CHARACTER SELECTION \nCHARACTER MUST BE  [[ X --or -- O ]]" )
                    time.sleep(2)
                    os.system('clear')
                    single_player()
                else:
                    if symbol == allowed[0] and symbol == allowed[1] and symbol == allowed[0].lower() and symbol == allowed[1].lower():
                       pass           
                    
                   
                
                    index=int(input("\n ENTER LOCATION TO PLAY  -----|   "))
                    
                    ai = random.choice(ai_choice)
                    if index == 1 :
                        ai_choice.remove(1)
                        if symbol.upper()=="X":
                            if position[0]=='X' or position[0]=='O':
                                print('\n-------WRONG MOVE')
                                time.sleep(2)
                               
                            elif position[0] !='X' or position[0] !='O':
                                position[0]= symbol.upper() 
                                position[ai-1]='O'
                                #del ai_choice[ai-1]
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[0]=='X' or position[0]=='O':
                                print('\n--------WRONG MOVE')
                                time.sleep(2)
                            
                             
                            elif position[0] !='X' or position[0] !='O':
                                position[0]= symbol.upper() 
                                position[ai-1]='X'
                                #del ai_choice[ai-1]
                                os.system('clear')
                                board()
                                win()
                            
                        
                    
                        
                    elif index == 2 :
                        ai_choice.remove(2)
                        if symbol.upper()=="X":
                            if position[1]=='X' or position[1]=='O':
                                print('\n-------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[1] !='X' or position[1] !='O':
                                position[1]= symbol.upper() 
                                position[ai-1]='O'
                                #del ai_choice[ai-1]
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[1]=='X' or position[1]=='O':
                                print('\n--------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[1] !='X' or position[1] !='O':
                                position[1]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                                
                    elif index == 3 :
                        ai_choice.remove(3)
                        if symbol.upper()=="X":
                            if position[2]=='X' or position[2]=='O':
                                print('\n-------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[2] !='X' or position[2] !='O':
                                position[2]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[2]=='X' or position[2]=='O':
                                print('\n-------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[2] !='X' or position[2] !='O':
                                position[2]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                                
                    elif index==4:
                        ai_choice.remove(4)
                        if symbol.upper()=="X":
                            if position[3]=='X' or position[3]=='O':
                                print('\n--------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[3] !='X' or position[3] !='O':
                                position[3]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[3]=='X' or position[3]=='O':
                                print('\n-------=---WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[3] !='X' or position[3] !='O':
                                position[3]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                                
                    elif index == 5:
                        ai_choice.remove(5)
                        if symbol.upper()=="X":
                            if position[4]=='X' or position[4]=='O':
                                print('\n--------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[4] !='X' or position[4] !='O':
                                position[4]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[4]=='X' or position[4]=='O':
                                print('\n---------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[4] !='X' or position[4] !='O':
                                position[4]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                    elif index == 6 :
                        ai_choice.remove(6)
                        if symbol.upper()=="X":
                            if position[5]=='X' or position[5]=='O':
                                print('\n----------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[5] !='X' or position[5] !='O':
                                position[5]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[5]=='X' or position[5]=='O':
                                print('\n---------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[5] !='X' or position[5] !='O':
                                position[5]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                    elif index == 7 :
                        ai_choice.remove(7)
                        if symbol.upper()=="X":
                            if position[6]=='X' or position[6]=='O':
                                print('\n----------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[6] !='X' or position[6] !='O':
                                position[6]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[6]=='X' or position[6]=='O':
                                print('\n---------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[6] !='X' or position[6] !='O':
                                position[6]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                    elif index == 8:
                        ai_choice.remove(8)
                        if symbol.upper()=="X":
                            if position[7]=='X' or position[7]=='O':
                                print('\n-------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[7] !='X' or position[7] !='O':
                                position[7]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[7]=='X' or position[7]=='O':
                                print('\n----------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[7] !='X' or position[7] !='O':
                                position[7]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()  
                                win()  
                    elif index == 9:
                        ai_choice.remove(9)
                        if symbol.upper()=="X":
                            if position[8]=='X' or position[8]=='O':
                                print('\n----------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[8] !='X' or position[8] !='O':
                                position[8]= symbol.upper() 
                                position[ai-1]='O'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()
                        elif symbol.upper()=="O":
                            if position[8]=='X' or position[8]=='O':
                                print('\n----------WRONG MOVE')
                                time.sleep(2)
                                board()
                            elif position[8] !='X' or position[8] !='O':
                                position[8]= symbol.upper() 
                                position[ai-1]='X'
                                #ai_choice.remove(ai)
                                os.system('clear')
                                board()
                                win()                           
                    
                   
                                                   
        except ValueError :
            print('\nLOCATION MUST BE INTEGER ')
            time.sleep(1)
            os.system('clear')
            board()




    

def win():
            if position[0] == position[3] == position[6] == 'X':
                print('\n-------YOU WIN PLAYER     X \n')
                option()
            elif position[1] == position[4] == position[7] == 'X':
                print('\n-------YOU WIN PLAYER     X  \n ')
                option()
            elif position[2] == position[5] == position[8] == 'X':
                print('\n---------YOU WIN PLAYER     X \n  ')
                option()
            elif position[0] == position[1] == position[2] == 'X':
                print('\n--------YOU WIN PLAYER     X \n ')
                option()
            elif position[3] == position[4] == position[5] == 'X':
                print('\n-------YOU WIN PLAYER     X \n ')
                option()
            elif position[6] == position[7] == position[8] == 'X':
                print('\n--------YOU WIN PLAYER     X \n ')
                option()
            elif position[0] == position[4] == position[8] == 'X':
                print('\n---------YOU WIN PLAYER     X \n ')
                option()
            elif position[2] == position[4] == position[6] == 'X':
                print('\n--------YOU WIN PLAYER     X \n ')
                option()
                
                
            elif position[0] == position[3] == position[6] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            elif position[1] == position[4] == position[7] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            elif position[2] == position[5] == position[8] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            elif position[0] == position[1] == position[2] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            elif position[3] == position[4] == position[5] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            elif position[6] == position[7] == position[8] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            elif position[0] == position[4] == position[8] == 'O':
                print('YOU WIN PLAYER     O')
                option()
            elif position[2] == position[4] == position[6] == 'O':
                print('YOU WIN PLAYER     O ')
                option()
            
            elif position[0] != 1 and position[1]!=2 and position[2] != 3 and position[3]!=4 and position[4] !=5 and position[5]!= 6 and position[6]!= 7 and position[7]!= 8 and position[8]!=9:
                    print('\n-----DRAW GAME \n--------------Nice Play ')
                    time.sleep(3)
                    os.system('clear')
                    option()
            


#single_player()  
option()                     
