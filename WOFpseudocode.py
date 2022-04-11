from pytest import MonkeyPatch


def indexall(pattern,word):
    return [index for index, value in enumerate(word) if value == pattern]
    #retrieved from stackoverflow.com

def split(word):
    return [char for char in word]
        #obtained from poopcode.com

def replace_clouded_letter(letter,answer,cloud):
    index_list = indexall(letter,answer)
    index_list_length = len(index_list)
    pos = 0
    while index_list_length > 0:
        cloud = split(cloud)
        cloud[index_list[pos]] = letter
        cloud = ''.join(cloud)
        index_list_length = index_list_length - 1
        pos = pos + 1
    return cloud
#compares hidden-word and dashed/clouded word and fills in letters that are guessed

def make_dashed_word(word):
    wordlen = len(word)
    emlist = []
    while wordlen > 0:
        emlist.append("-")
        wordlen = wordlen - 1
    dashed_word = ''.join(emlist)
    return dashed_word
#returns a dashed word of same length as target word

#def is_legal_consonant:
    ###

#def is_legal_vowel:
    ###

#i need a function that takes the hidden-word and clouded word, copies the hidden word and dashes the unclouded letters from the clouded word on that copy

#ill start with a function that removes all dashes from a clouded word

def remove_word_clouds(clouded_word):
    split_list = split(clouded_word)
    cycles = len(split_list)
    pos = 0
    while cycles > 0:
        if split_list[pos] == '-':
            split_list[pos] = ' ' 
            pos = pos + 1
            cycles = cycles - 1
        else:
            pos = pos + 1
            cycles = cycles - 1
    split_list = ''.join(split_list)
    split_list.replace(' ','')
    return split_list

print(remove_word_clouds('c--l'))

def anti_clouded_word(hidden_word,clouded_word):
    index_list = []
    unclouded_word = remove_word_clouds(clouded_word)
    for letter in unclouded_word:
        index_list = index_list + indexall(letter,hidden_word)
    hidden_list = split(hidden_word)
    for num in index_list:
        hidden_list[num] = '-'
    return ''.join(hidden_list)

def count_consonants(word):
    word = word.lower()
    word = split(word)
    cycles = len(word)
    pos = 0
    count = 0
    while cycles > 0:
        if word[pos] in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
            count = count + 1
            pos = pos + 1
            cycles = cycles - 1
        else:
            pos = pos + 1
            cycles = cycles - 1
    return count

#so here im gonna make a function that takes a word and returns true if only values

def only_vowels(word):
    count = count_consonants(word)
    if count == 0:
        return True
    else:
        return False

#use this function and make another function that returns True if its zero

final_bank = {'1':0,'2':0,'3':0}
temp_bank = {'1':0, '2':0, '3':0}
players = ['1','2','3']

def guess_answer(hidden_word, clouded_word, playerint):
      guess = input(clouded_word + ' Make your guess: ')
      if guess.lower() == hidden_word:
        #print('congradulations, that's it!! You've won player' + -> temp_bank[player] + '$!')
        #return True
      #else:
        #print('Incorect')
        #return False

current_player = 1
round = 1

#if a word is down to values gameplay takes place of guessing values

#while round is one or two:
    
    #if round = 2:
        #current player = int(sorted(perm_bank.items(), key=lambda x: x[1])[0][0]
    #HIDDEN WORRD = random.choice(word_list)
    #clouded_word = make_dashed_word(HIDDEN WORD)
    #while Hidden word not eq clouded-word???:
        #turn_is_over = False????
        #hidden_word_unguessed_letter_only = remove_word_clouds((anti_clouded_word(hidden_word,clouded_word)))
        
        #if not only_vowels(hidden_word_unguessed_letters_only):
        #next_player moves the player-number forward, resetting to '1' after '3'
        

            #input('it is your turn player ' + current_player + '! Enter anykey to spin!
            # or enter 'solve' to answer the puzzle')

            #if input.lower() == 'solve':
                #if guess_answer(hidden_word, clouded_word, player(int)):
                    #player -> perm_bank[str(currentplayer)] = temp_bank.get(str(current_player))
                    #temp_bank['1] = 0
                    #temp_bank['2] = 0
                    #temp_bank['3] = 0
                    #break
                #else:
                    #next playyer()
                    #turn is over
                    #continue
            #wheel = a list of 24 strings containing BANKRUPT, Lose-Turn and several cash values

            #wheel_result = random.choose(wheel)
        
            #so, I need to skip phase 1 if no consonants remain in the function
            #turn_is_over = False
        
        #elif only_vowels(hidden_word_unguessed_letters_only):
            #print('Note, there are only vowels remaining.')
            #only_vowels = True

        #PHASE 1
        #while not turn_is_over AND not only_vowels:
            #if count(consonants = 0):???
                #game_phase_1 = False???
            #PHASE 1
            #if wheel_result is BANKRUPT
                #print(wheel_result + '! ooh bad luck! but the game isn't over until it's over!)
                #current_player -> bank[str(current_player)] = 0
                #next_player
                #turn is over = True
                #break
            #elif wheel_result is Lose-Turn
                #print(wheel_result + '! Next turn!')
                #next_player
                #turn is over = True
                #break
            #else:
                #consonent_guess = input('Guess a consonant and win ' + int(wheel_result) + '$ for every time it appears in the word.')
            
                #is_legal_consonant -- a function that returns true if an input is a valid consonant and false if it isn't

                #if is_legal_consonant(consonant_guess):
                    #if clouded_word IS-EQUAL-TO replace_clouded_letter:
                        #(clouded_word + 'sorry, no help there!)
                        #next player
                        #turn is over = True
                        #break
                    #elif clouded_word IS-NOT-EQUAL-To replace_clouded_letter:
                        #clouded_word = replace_clouded_letter(input,hidden_word,clouded_word)
                        #letter_index = index(*consonent,clouded_word)
                        #nubmer_of_sucesses = len(letter_index)
                        #money_earned = int(wheel_result) * number_of_sucesses
                        ##current_player -> temp_bank[player] = temp_bank[player] + (int(wheel_result) * number_of_sucesses)
                        #print('word so far is ' + clouded_word' + '! ' + money_earned + '$ to the bank!)
                        
                        #hidden_word_unguessed_letter_only = remove_word_clouds((anti_clouded_word(hidden_word,clouded_word)))
                        #if only_vowels(hidden_word_unguessed_letters_only):
                            #print('Note. There are only vowels remaining!')
                            ####break  -to the next phase
                        #else:
                            ####break  -to the next phase
                #elif not is_legal_consonant:
                    #print('that is not a consonant. Try again.')
                    #restart loop
                    #continue
                #can delete this probably#current_player -> bank[player] + int(wheel_result)
        #PHASE 2
        #while not turn_is_over:
            #input_is_legal = False???
            #while not input_is_legal:???
            #phase2_input = input('Now' + current_player + 'would you like to pay 250$ for the chance reveal a vowel, or would you like to try and solve the puzzle? Your current balance for this round is' + temp_bank[player] + '$. Enter \'pay\' to buy a vowel or \'solve\' to guess the puzzle :')
            #if phase2_input.lower() == 'solve':
                #guess_input = input(clouded_word + ' Enter your guess: ')
                #if guess_answer(hidden_word, clouded_word, player(int)):
                    #player -> perm_bank[str(currentplayer)] = temp_bank.get(str(current_player))
                    #temp_bank['1] = 0
                    #temp_bank['2] = 0
                    #temp_bank['3] = 0
                    #break
                #else:
                    #next playyer()
                    #turn is over = True
                    #break
            #elif phase2_input.lower() == 'pay':
                #if player -> temp_bank[str(player] >= 250:
                    #vowel_guess = input('Enter your vowel: ')
                    #if is_legal_vowel(vowel_guess):
                        #player -> temp_bank[str(player)] = -250
                        #if clouded_word IS-EQUAL-TO replace_clouded_letter:
                            #(clouded_word + 'sorry, no help there!)
                            #next player
                            #turn is over = True
                            #break I think to break the loop and go to next player
                        #else:
                            #clouded_word = replace_clouded_letter(input,hidden_word,clouded_word)
                            #letter_index = index(*consonent,clouded_word)
                            #print('word so far is ' + clouded_word' + '! ' + 'you're getting closer!)
                            #continue
                #else:
                    #print('You do not have enough money to buy a vowel this turn. Enter your guess for the puzzle, instead:')
                    #guess_input = input(clouded_word + ' Enter your guess: ')
                    #if guess_answer(hidden_word, clouded_word, player(int)):
                        #player -> perm_bank[str(currentplayer)] = temp_bank.get(str(current_player))
                        #temp_bank['1] = 0
                        #temp_bank['2] = 0
                        #temp_bank['3] = 0
                        #break
                    #else:
                        #next playyer()
                        #turn is over = True
                        #break
            #else:
                #print('your input must be \'solve\' or \'pay\', you skalliwag!')
                #continue

                #need to test if the vowel is correct, and only afterwards subtract the money, ooh i need to check if they do have money first
                #check money
                #make sure its a correct vowel and have them enter again if it isn't
                #is the vowel in the hidden word, if so restart phase 2, if not end the turn
            
        #if turn_ovrr:
            #next player
            #continue  
        #else:
            #break
    #print('This round is finished, here are the standings\nPlayer 1 has' + perm_bank.get('1') + '$, Player 2 has' + perm_bamnk.get(('2') + '$, and Player 3 has ' + perm_bank.get('3') + '$.)))   
    #sort dictioary so who is in the lead is first, this person starts next round. get the item where the value is highest
    #(sorted(perm_bank.items(), key=lambda x: x[1])[0][0]
    #round = round + 1
    # continue     
#FINAL ROUND
#current player = int(sorted(perm_bank.items(), key=lambda x: x[1])[0][0]
#hidden_word = random.choice(word_list)
#clouded_word = make_dashed_word(HIDDEN WORD)
#free_letters = ['r','s','t','l','n','e']
#for letter in free_letters:
    #clouded_word = replace_clouded_letter(letter,answer,cloud)
#print('Congradulations, Player' + current_player + ", you have made it to the final round. Currently you have " + player -> str(perm_bank[current_player]) '$ But you COULD go home with ' + str(perm_bank[current_player]+1000000) + '$! Let's play!)
#print('Your word so far is' + clouded_word + ' you may enter three more consonants and a vowel before guessing the answer.)
#consonant_guesses = 0
#vowel_guesses = 0
#while consonant_guesses < 3 AND vowel_guesses < 1:
    #if consonant_guesses > 3:
        #consonant_guesses = consonant_guesses - 1
        #print('you can't add anymore consonants.)
        #continue
    #elif vowel_guesses > 1:
        #vowel_guesses = vowel_guesses - 1
        #print(you can't add anymore consonants)
        #continue
    #else:
        #letter_input = input('enter a value)
        #if letter_input not LEGAL_LETTER:
            #print(that's not a letter.)
            #continue
        #elif letter_input CONSONANT:
            #consonant_guesses = consonant_guesses + 1
            ##if consonant_guesses > 3:
                #consonant_guesses = consonant_guesses - 1
                #print('you can't add anymore consonants.)
                #continue
            #else:
                #clouded_word = replace_clouded_letter(letter_input, hidden_word, clouded_word)
                #consonant_guesses = consonant_guesses + 1
        #elif letter_input VOWEL:
            #vowel_guesses = vowel_guesses + 1
            ##if vowel_guesses > 1:
                #vowel_guesses = vowel_guesses - 1
                #print('you can't add anymore vowels'.)
                #continue
            #else:
                #clouded_word = replace_clouded_letter(letter_input, hidden_word, clouded_word)
                #vowel_guesses = vowel_guesses + 1
#final_guess = input('The word so far is ' + clouded_word + '. You have 30 seconds to make your final guess.\nYour final answer: ')
#if final_guess.lower() == hidden_word:
    #print('Congradulations! You have guessed corrently and won 1,000,000 dollars!')
    #player -> perm_bank[current_player] = perm_bank[current_player] + 1000000
    #print('The final scores are Player 1:' + player -> perm_bank['1'] + '$, Player 2: ' + perm_bank['2'] + '$, Player 3: ' + perm_bank['3'] + '$')
#else:
    #print('so sorry but that's not the answer. Still! You've won ' + perm_bank[current_player] + '$! Thanks for playing!')
    #print('The final scores are Player 1:' + player -> perm_bank['1'] + '$, Player 2: ' + perm_bank['2'] + '$, Player 3: ' + perm_bank['3'] + '$')



            


tuple = [(1,1),(3,2),(2,3)]
print(tuple[0][0])
testdict = {'A':1,'C':2,'B':3,'D':0}
print((sorted(testdict.items(), key=lambda x: x[1])[0][0]))


print(split('about'))
listo = split('about')
listo.remove('o')
print(listo)

print(remove_word_clouds('l-s-r'))
print(remove_word_clouds((anti_clouded_word('school','s-h--l'))))