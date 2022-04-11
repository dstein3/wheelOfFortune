import random
import time

#random.seed(130)

f = open(r"words_alpha.txt")
word_list = f.readlines()
f.close()
print(len(word_list))
word = random.choice(word_list)

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

#word = 'pretty'
#cloud = 'pre--y'
#print(replace_clouded_letter('r',word,cloud))
#print(cloud)

def make_dashed_word(word):
    wordlen = len(word)
    emlist = []
    while wordlen > 0:
        emlist.append("-")
        wordlen = wordlen - 1
    dashed_word = ''.join(emlist)
    return dashed_word
#returns a dashed word of same length as target word

def is_legal_consonant(letter):
    if len(letter) > 1:
        return False
    elif letter.lower() in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        return True
    else:
        return False

def is_legal_vowel(letter):
    if len(letter) > 1:
        return False
    elif letter.lower() in ['a','e','i','o','u']:
        return True
    else:
        return False

def remove_word_clouds(clouded_word):
    split_list = split(clouded_word)
    split_list = [value for value in split_list if value != '-']
    split_list = ''.join(split_list)
    return split_list
#built using help from freecodecamp.com

def anti_clouded_word(hidden_word,clouded_word):
    index_list = []
    unclouded_word = remove_word_clouds(clouded_word)
    for letter in unclouded_word:
        index_list = index_list + indexall(letter,hidden_word)
    hidden_list = split(hidden_word)
    for num in index_list:
        hidden_list[num] = '-'
    return ''.join(hidden_list)
#return the opposite of the cloud for a hidden word. used to evaluate if the unguessed letters in a word are all vowels, or not

#print(anti_clouded_word('noise','n---e'))

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

#print(count_consonants('aaa'))

def count_vowels(word):
    word = word.lower()
    word = split(word)
    cycles = len(word)
    pos = 0
    count = 0
    while cycles > 0:
        if word[pos] in ['a','e','i','o','u']:
            count = count + 1
            pos = pos + 1
            cycles = cycles - 1
        else:
            pos = pos + 1
            cycles = cycles - 1
        return count

def legal_letter(value):
    if len(value) == 1 and value.lower() in ['a','e','i','o','u','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']:
        return True
    else:
        return False

#print(legal_letter('aaa'))
#print(legal_letter('b'))
#print(legal_letter('a'))
#print(legal_letter('2'))
#print(count_vowels('ppp'))

def only_vowels(word):
    if word == '':
        return False
    else:
        countC = count_consonants(word)
        countV = count_vowels(word)
        if countC == 0 and countV > 0:
            return True
        else:
            return False

#print(only_vowels('aaa'))
#print(only_vowels('bbb'))
#print(only_vowels(''))
#perm_bank = {'1':100,'2':10000,'3':1000}
#print(int(sorted(perm_bank.items(), key=lambda x: x[1])[2][0]))
#print(sorted(perm_bank.items(), key=lambda x: x[1]))

hidden_word = 'talent'
clouded_word = 'tal--t'
print(remove_word_clouds((anti_clouded_word(hidden_word,clouded_word))))

def guess_answer(hidden_word, clouded_word, playerint, bank):
    guess = input('Word so far: \'' + clouded_word + '\'\nMake your guess: ')
    if guess.lower() == hidden_word:
        print('Congradulations Player ' + str(playerint) + ', that\'s it!! The answer was \'' + hidden_word + '\'! You\'ve won ' + str(bank[str(playerint)]) + '$!')
        return True
    else:
        print('Incorrect.')
        return False

players = [1,2,3]

def player_rotation(current_player):
    players = [1,2,3]
    index = players.index(current_player)
    pos = index
    pos = pos + 2
    if pos == 4:
        pos = 1
    return pos

#print(player_rotation(1))
#print(player_rotation(2))
#print(player_rotation(3))

#wheel_pool = [100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900]
#(wheel_pool)
#print(len(wheel_pool))
#wheel = []
#print(wheel)
#temp_bank = {'1':100, '2':10000, '3':1000}
#temp_bank['1'] = temp_bank['1']+17
#print(temp_bank)
#print(sorted(temp_bank.items(), key=lambda x: x[1])[2][0])
#print(sorted(temp_bank.items(), key=lambda x: x[1]))

#answer = 'terminate'
#clouded_word = '---------'

#free_letters = ['r','s','t','l','n','e']
#for letter in free_letters:
    #clouded_word = replace_clouded_letter(letter,answer,clouded_word)

#print(clouded_word)

def wheelOfFortune():
    print('Welcome to wheel of fortune! For the first two rounds, you and your friends will guess a hidden word for a chance to win money.\nGuess the word and you keep all the money you earned that round.\nWhoever has the most money after two rounds will have the chance to earn 1,000,000$!')
    perm_bank = {'1':0,'2':0,'3':0}
    temp_bank = {'1':0, '2':0, '3':0}
    current_player = 1
    round = 1
    wheel = ['Lose a Turn', 650, 350, 150, 750, 450, 550, 750, 300, 450, 400, 600, 800, 750, 250, 150, 900, 100, 800, 900, 900, 650, 450,'BANKRUPT']
    while round == 1 or round == 2:
        if round == 2:
            if perm_bank['1'] == perm_bank['2'] == perm_bank['3']:
                current_player = player_rotation(current_player)
            else:
                current_player = int(sorted(perm_bank.items(), key=lambda x: x[1])[2][0])
        hidden_word = random.choice(word_list)
        #hidden_word = 'aaa'
        hidden_word = hidden_word.strip()
        clouded_word = make_dashed_word(hidden_word)
        #while hidden_word != clouded_word:
        while hidden_word != clouded_word:
            turn_is_over = False
            hidden_word_unguessed_letter_only = remove_word_clouds((anti_clouded_word(hidden_word,clouded_word)))
            if not only_vowels(hidden_word_unguessed_letter_only):
                only_vowels_left = False
                input_spin_solve = input('It is your turn, Player ' + str(current_player) + '! The word, so far, is \'' + clouded_word + '\'. Enter anykey to spin, or \'solve\' to guess the hidden-word: ')
                print('For the grader: the hidden_word is \'' + hidden_word + '\'.')
                if input_spin_solve.lower() == 'solve':
                    if guess_answer(hidden_word, clouded_word, current_player, temp_bank):
                        #perm_bank[str(current_player)] = temp_bank.get(str(current_player))
                        #temp_bank['1'] = 0
                        #temp_bank['2'] = 0
                        #temp_bank['3'] = 0
                        #print(perm_bank)
                        #round = round + 1
                        break
                    else:
                        current_player = player_rotation(current_player)
                        turn_is_over = True
                        continue
                else:
                    print('Spinning!!')
                    wheel_result = random.choice(wheel)
                    print(wheel_result)
            elif only_vowels(hidden_word_unguessed_letter_only):
                print('Note, there are only vowels remaining.')
                only_vowels_left = True
            else:
                print('error phase-0')
                break
            #PHASE 1
            while not turn_is_over and not only_vowels_left:
                #wheel_result = random.choice(wheel)
                #wheel_result = 'Lose a Turn'
                if wheel_result == 'BANKRUPT':
                    print(wheel_result + '! ooh bad luck! but the game isn\'t over until it\'s over!')
                    temp_bank[str(current_player)] = 0
                    current_player = player_rotation(current_player)
                    turn_is_over = True
                    break
                elif wheel_result == 'Lose a Turn':
                    print(wheel_result + '! Next turn!')
                    current_player = player_rotation(current_player)
                    turn_is_over = True
                    break
                else:
                    consonent_guess = input('Word so far: ' + clouded_word + '\nGuess a consonant and win ' + str(wheel_result) + '$ for every time it appears in the word!\nP.S, \'y\' is a consonant, here: ')
                    if is_legal_consonant(consonent_guess):
                        print('cool')
                        if clouded_word == replace_clouded_letter(consonent_guess,hidden_word,clouded_word):
                            print(clouded_word + '\nsorry, no help there!')
                            current_player = player_rotation(current_player)
                            turn_is_over = True
                            break
                        elif clouded_word != replace_clouded_letter(consonent_guess,hidden_word,clouded_word):
                            clouded_word = replace_clouded_letter(consonent_guess,hidden_word,clouded_word)
                            letter_index = indexall(consonent_guess,hidden_word)
                            number_of_sucesses = len(letter_index)
                            money_earned = wheel_result * number_of_sucesses
                            temp_bank[str(current_player)] = temp_bank[str(current_player)] + (wheel_result * number_of_sucesses)
                            ##current_player -> temp_bank[player] = temp_bank[player] + (int(wheel_result) * number_of_sucesses)
                            print('The word so far is ' + clouded_word + '! ' + str(money_earned) + '$ to the bank!')
                            hidden_word_unguessed_letter_only = remove_word_clouds((anti_clouded_word(hidden_word,clouded_word)))
                            if only_vowels(hidden_word_unguessed_letter_only):
                                print('Note. There are only vowels remaining!')
                                break
                            else:
                                break
                    elif not is_legal_consonant(consonent_guess):
                        print('That\'s not a consonant. Try again.')
                        continue
            #PHASE 2
            while not turn_is_over:
                phase2_input = input('\nNow Player ' + str(current_player) + ', would you like to pay 250$ for the chance reveal a vowel?\nOr would you like to try and solve the puzzle?\n\nYour current balance for this round is ' + str(temp_bank[str(current_player)]) + '$. The word, so far, is \'' + clouded_word + '\'\nEnter \'pay\' to buy a vowel or \'solve\' to guess the puzzle: ')
                if phase2_input.lower() == 'solve':
                    print('For the grader: the hidden_word is \'' + hidden_word + '\'.')
                    #vowel_guess = input(clouded_word + ' Enter your guess: ')
                    if guess_answer(hidden_word, clouded_word, current_player,temp_bank):
                        #perm_bank[str(current_player)] = temp_bank[str(current_player)]
                        #temp_bank['1'] = 0
                        #temp_bank['2'] = 0
                        #temp_bank['3'] = 0
                        #round = round + 1
                        break
                    else:
                        current_player = player_rotation(current_player)
                        turn_is_over = True
                        break
                elif phase2_input.lower() == 'pay':
                    if temp_bank[str(current_player)] >= 250:
                        vowel_guess = input('Enter your vowel: ')
                        if is_legal_vowel(vowel_guess):
                            temp_bank[str(current_player)] = temp_bank[str(current_player)] - 250
                            if clouded_word == replace_clouded_letter(vowel_guess,hidden_word,clouded_word):
                                print(clouded_word + 'Sorry, no help there!')
                                current_player = player_rotation(current_player)
                                turn_is_over = True
                                break
                            else:
                                clouded_word = replace_clouded_letter(vowel_guess,hidden_word,clouded_word)
                                #letter_index = index(*consonent,clouded_word)
                                print('The word, so far, is ' + clouded_word + '! You\'re getting closer!\n')
                                continue
                    else:
                        print('You do not have enough money to buy a vowel this turn. Enter your guess for the puzzle, instead:')
                        #guess_input = input(clouded_word + ' Enter your guess: ')
                        print('For the grader: the hidden_word is \'' + hidden_word + '\'.')
                        if guess_answer(hidden_word, clouded_word, current_player):
                            #perm_bank[str(current_player)] = temp_bank[str(current_player)]
                            #temp_bank.get(str(current_player))
                            #temp_bank['1'] = 0
                            #temp_bank['2'] = 0
                            #temp_bank['3'] = 0
                            #round = round + 1
                            break
                        else:
                            print('incorrect')
                            current_player = player_rotation(current_player)
                            turn_is_over = True
                            break
                else:
                    print('Your input must be \'solve\' or \'pay\'')
                    continue
            if turn_is_over:
                continue
            else:
                #print('begin_phase_2')
                break
        #print('The word is \'' + hidden_word + '\'! Congradulations Player ' + str(current_player) + ', you have just won ' + str(temp_bank[str(current_player)]) + '$!')    
        perm_bank[str(current_player)] = perm_bank[str(current_player)] + temp_bank[str(current_player)]
        temp_bank['1'] = 0
        temp_bank['2'] = 0
        temp_bank['3'] = 0
        print('This round is finished. Here are the standings\nPlayer 1 has ' + str(perm_bank.get('1')) + '$, Player 2 has ' + str(perm_bank.get('2')) + '$, and Player 3 has ' + str(perm_bank.get('3')) + '$.')
        #sort dictioary so who is in the lead is first, this person starts next round. get the item where the value is highest
        #current_player = int(sorted(perm_bank.items(), key=lambda x: x[1])[2][0])
        round = round + 1
        continue
    #FINAL ROUND
    current_player = int(sorted(perm_bank.items(), key=lambda x: x[1])[2][0])
    second_place_player = int(sorted(perm_bank.items(), key=lambda x: x[1])[1][0])
    third_place_player = int(sorted(perm_bank.items(), key=lambda x: x[1])[0][0])
    if perm_bank[str(current_player)] == perm_bank[str(second_place_player)] or perm_bank[str(current_player)] == perm_bank[str(third_place_player)]:
        print('Wow a tie, that\'s sad. No one gets a million dollars in round three.')
    else:
        hidden_word = random.choice(word_list)
        hidden_word = hidden_word.lower()
        hidden_word = hidden_word.strip()
        clouded_word = make_dashed_word(hidden_word)
        free_letters = ['r','s','t','l','n','e']
        for letter in free_letters:
            clouded_word = replace_clouded_letter(letter,hidden_word,clouded_word)
        print('Congradulations, Player' + str(current_player) + ", you have made it to the final round. Currently you have " + str(perm_bank[str(current_player)]) + '$ But you COULD go home with ' + str(perm_bank[str(current_player)] + 1000000) + '$! Let\'s play!')
        print('Your word so far is \'' + clouded_word + '\'. You may enter three more consonants and a vowel before guessing the answer.')
        consonant_guesses = 0
        vowel_guesses = 0
        while consonant_guesses < 3 or vowel_guesses < 1:
            print('Word so far: ' + clouded_word)
            letter_input = input('Enter a letter: ')
            if not legal_letter(letter_input):
                print('That\'s not a letter.')
                continue
            elif is_legal_consonant(letter_input):
                if consonant_guesses >= 3:
                    print('You can\'t add anymore consonants.')
                    continue
                elif letter_input in free_letters:
                    print('that letter has already been guessed')
                    continue
                else:
                    clouded_word = replace_clouded_letter(letter_input, hidden_word, clouded_word)
                    free_letters.append(letter_input)
                    consonant_guesses = consonant_guesses + 1
                    continue
            elif is_legal_vowel(letter_input):
                if vowel_guesses >= 1:
                    print('You can\'t add anymore vowels.')
                    continue
                elif letter_input in free_letters:
                    print('that letter has already been guessed')
                    continue
                else:
                    clouded_word = replace_clouded_letter(letter_input, hidden_word, clouded_word)
                    free_letters.append(letter_input)
                    vowel_guesses = vowel_guesses + 1
                    continue
        print('For the grader: the hidden_word is \'' + hidden_word + '\'.')
        final_guess = input('The word so far is ' + clouded_word + '. Make your final guess.\nYour final answer: ')
        if final_guess.lower() == hidden_word:
            print('Congradulations! You have guessed corrently and won 1,000,000 dollars!')
            perm_bank[str(current_player)] = perm_bank[str(current_player)] + 1000000
            print('The final scores are Player 1:' + str(perm_bank['1']) + '$, Player 2: ' + str(perm_bank['2']) + '$, Player 3: ' + str(perm_bank['3']) + '$')
        else:
            print('So sorry but that\'s not the answer. Still! You\'ve won ' + str(perm_bank[str(current_player)]) + '$! Thanks for playing!')
            print('The final scores are Player 1:' + str(perm_bank['1']) + '$, Player 2: ' + str(perm_bank['2']) + '$, Player 3: ' + str(perm_bank['3']) + '$')

    

        #print('Round is over!')
        #print(perm_bank)   
        #break
        #continue


            #if turn_is_over:
            #    continue
            #else:
                #print('begin_phase_2')
            #    break   
        
    #print('test done')
                #else:
                    #print('not BANKRUPT')
                    #break
        #break
    #print('test done')


wheelOfFortune()




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
        

            #input_spinsolve = input('it is your turn player ' + current_player + '! Enter anykey to spin!
            # or enter 'solve' to answer the puzzle')

            #if input_spinsolve.lower() == 'solve':
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

#wheelOfFortune()