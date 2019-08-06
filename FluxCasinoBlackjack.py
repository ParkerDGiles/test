# Blackjack Card Game - Flux Casino
def space():
    print(' \n ')
def returntomain():
    space()
    print('Would you like to return to the main menu or exit?')
    print('Return to main menu = y   Exit = n')
    exitanswer = input()
    if exitanswer == 'n':
        print('Exiting game...')
        exit()
    if exitanswer == 'y':
        print('Directing to main menu...')
        main()
    else:
        print('Please check your answer and try again: ')
        returntomain()
def quitgame():
    space()
    print('Are you sure you would like to exit the game?')
    print ('Yes = y   No = n')
    exitanswer = input()
    if exitanswer == 'y':
        print('Exiting game...')
        exit()
    if exitanswer == 'n':
        print('Directing to main menu...')
        main()
    else:
        print('Please check your answer and try again: ')
        quitgame()
def gamerules():
    space()
    print('The goal of blackjack is to get as close as possible to 21 with the sum of your cards.')
    print('The player will buy-in with $5,000 and have a low of 100 and a high of $100,000.')
    print('All cards are worth their number, with jacks, queens, and kings as 10, and Aces as 1 or 11')
    print('Player will receive double their bet if won, and a 10% bonus if player wins with a blackjack.')
    print('Player receives a blackjack if the first hand is equal to 21, a blackjack beats a counted 21.')
    print('Dealer will stand on 17')
    returntomain()
def scoreboard():
    space()
    print('    Flux Casino Blackjack Records')
    print('$--$--$--$--$--$--$--$--$--$--$--$--$')
    print('1. Mr. Jack         -- $10,000,000')
    print('2. Lil Miss Diamond --  $7,500,000')
    print('3. Terry Ace        --  $5,000,000')
    print('4. Kingman Harry    --  $2,500,000')
    print('5. Jack Daniel      --  $1,000,000')
    print('6. Jester Julie     --    $750,000')
    print('7. Tin Ten          --    $500,000')
    print('8. Low Roller       --    $250,000')
    print('9. Lucky Rick       --    $100,000')
    print('10. Hobo Jones      --     $50,000')
    returntomain()
def greeting():
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Let us begin.')
    if rr == 2:
        print('Dealer: How about we get some cards out here.')
    if rr == 3:
        print('Dealer: Best of luck to you.')
    if rr == 4:
        print('Dealer: Let us see how this round plays out.')
def anothercard():
    space()
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Would you like another card?')
    if rr == 2:
        print('Dealer: Another one?')
    if rr == 3:
        print('Dealer: Take another card?')
    if rr == 4:
        print('Dealer: How about one more?')
    space()
    print('Hit - h   Stand - s   Exit - e')
def placebet():
    print('You currently have', chips, 'chips')
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Please place your bets.')
    if rr == 2:
        print('Dealer: Round about to begin, place your bets.')
    if rr == 3:
        print('Dealer: Lets see those bets.')
    if rr == 4:
        print('Dealer: Whats gonna be the bet this round?')
def nomorebets():
    space()
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Bets are now cosed.')
    if rr == 2:
        print('Dealer: No more bets.')
    if rr == 3:
        print('Dealer: Betting is now closed.')
    if rr == 4:
        print('Dealer: Bets closed.')
def endgame():
    print('Dealer: Thanks for playing at Flux Casino.')
    space()
    if chips > 50000 < 100000:
        print('You placed 10th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 9th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 8th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 7th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 6th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 5th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 4th place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 3rd place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 2nd place on the scoreboard!')
    if chips > 50000 < 100000:
        print('You placed 1st place on the scoreboard!')
    quitgame()
def winner():
    global chips
    global c1, c2, c3, c4
    global bet
    space()
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Looks like we got a winner.')
    if rr == 2:
        print('Dealer: You beat the house this time.')
    if rr == 3:
        print('Dealer: We got a winner here.')
    if rr == 4:
        print('Dealer: There we have it folks, a winner.')
    chips = int((chips +(bet*2)))
    play()
def cards1():
    global chips
    global c1, c2, c3, c4
    global bet
    if c1 == 1:
        print('You received an Ace')
    if c1 == 2:
        print('You received a 2')
    if c1 == 3:
        print('You received a 3')
    if c1 == 4:
        print('You received a 4')
    if c1 == 5:
        print('You received a 5')
    if c1 == 6:
        print('You received a 6')
    if c1 == 7:
        print('You received a 7')
    if c1 == 8:
        print('You received an 8')
    if c1 == 9:
        print('You received a 9')
    if c1 == 10:
        print('You received a 10')
    if c1 == 11:
        print('You received a Jack')
    if c1 == 12:
        print('You received a Queen')
    if c1 == 13:
        print('You received a King')
    if c2 == 1:
        print('The Dealer received an Ace')
    if c2 == 2:
        print('The Dealer received a 2')
    if c2 == 3:
        print('The Dealer received a 3')
    if c2 == 4:
        print('The Dealer received a 4')
    if c2 == 5:
        print('The Dealer received a 5')
    if c2 == 6:
        print('The Dealer received a 6')
    if c2 == 7:
        print('The Dealer received a 7')
    if c2 == 8:
        print('The Dealer received an 8')
    if c2 == 9:
        print('The Dealer received a 9')
    if c2 == 10:
        print('The Dealer received a 10')
    if c2 == 11:
        print('The Dealer received a Jack')
    if c2 == 12:
        print('The Dealer received a Queen')
    if c2 == 13:
        print('The Dealer received a King')
    if c3 == 1:
        print('You received an Ace')
    if c3 == 2:
        print('You received a 2')
    if c3 == 3:
        print('You received a 3')
    if c3 == 4:
        print('You received a 4')
    if c3 == 5:
        print('You received a 5')
    if c3 == 6:
        print('You received a 6')
    if c3 == 7:
        print('You received a 7')
    if c3 == 8:
        print('You received an 8')
    if c3 == 9:
        print('You received a 9')
    if c3 == 10:
        print('You received a 10')
    if c3 == 11:
        print('You received a Jack')
    if c3 == 12:
        print('You received a Queen')
    if c3 == 13:
        print('You received a King')
    if c1 + c3 == 21:
        print('Dealer: We got a Blackjack')
    print('Dealer received their 2nd card.')
    if (c2 + c4) == 21 and (c1 + c3) == 21:
        print('Looks like we are all tied up.')
        print('Chips have been pushed.')
        chips = int((chips + bet))
        play()
    if (c2 + c4) > 21 and (c1 + c3) == 21:
        bonus = float(bet * .10)
        chips = int((chips + bet) + bonus)
        print('Dealer: We got a nice win here.')
        play()
def bust():
    global chips
    global bet
    space()
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Looks like the house wins this one.')
    if rr == 2:
        print('Dealer: Bust.')
    if rr == 3:
        print('Dealer: We got a bust.')
    if rr == 4:
        print('Dealer: Thats a bust.')
    play()
def hit4():
    global c1, c2, c3, c4, c5, c7, c9, c11
    global bet
    import random
    global playercount
    low = (1)
    high = (14)
    ran_number11 = random.uniform(low, high)
    c11 = (int(ran_number11))
    if c11 == 1:
        print('You received an Ace')
    if c11 == 2:
        print('You received a 2')
    if c11 == 3:
        print('You received a 3')
    if c11 == 4:
        print('You received a 4')
    if c11 == 5:
        print('You received a 5')
    if c11 == 6:
        print('You received a 6')
    if c11 == 7:
        print('You received a 7')
    if c11 == 8:
        print('You received an 8')
    if c11 == 9:
        print('You received a 9')
    if c11 == 10:
        print('You received a 10')
    if c11 == 11:
        print('You received a Jack')
    if c11 == 12:
        print('You received a Queen')
    if c11 == 13:
        print('You received a King')
    playercount = int((c1 + c3 + c5 + c7 + c9 + c11))
    if (c1 + c3 + c5 + c7 + c9 + c11) > 21:
        bust()
    anothercard()
    resp = input()
    if resp == 'h':
        print('Okay, I do not wanna write any more code for the next time you somehow need more than 6 cards.')
        print('I admire you of beating odds and making it this far so I will let you win this round.')
        winner()
    if resp == 's':
        stand()
    if resp == 'e':
        endgame()
def hit3():
    global c1, c2, c3, c4, c5, c7, c9
    global bet
    import random
    global playercount
    low = (1)
    high = (14)
    ran_number9 = random.uniform(low, high)
    c9 = (int(ran_number9))
    if c9 == 1:
        print('You received an Ace')
    if c9 == 2:
        print('You received a 2')
    if c9 == 3:
        print('You received a 3')
    if c9 == 4:
        print('You received a 4')
    if c9 == 5:
        print('You received a 5')
    if c9 == 6:
        print('You received a 6')
    if c9 == 7:
        print('You received a 7')
    if c9 == 8:
        print('You received an 8')
    if c9 == 9:
        print('You received a 9')
    if c9 == 10:
        print('You received a 10')
    if c9 == 11:
        print('You received a Jack')
    if c9 == 12:
        print('You received a Queen')
    if c9 == 13:
        print('You received a King')
    playercount = int((c1 + c3 + c5 + c7 + c9))
    if (c1 + c3 + c5 + c7 + c9) > 21:
        bust()
    anothercard()
    resp = input()
    if resp == 'h':
        hit4()
    if resp == 's':
        stand()
    if resp == 'e':
        endgame()
def hit2():
    global c1, c2, c3, c4, c5, c7
    global bet
    import random
    global playercount
    low = (1)
    high = (14)
    ran_number7 = random.uniform(low, high)
    c7 = (int(ran_number7))
    if c7 == 1:
        print('You received an Ace')
    if c7 == 2:
        print('You received a 2')
    if c7 == 3:
        print('You received a 3')
    if c7 == 4:
        print('You received a 4')
    if c7 == 5:
        print('You received a 5')
    if c7 == 6:
        print('You received a 6')
    if c7 == 7:
        print('You received a 7')
    if c7 == 8:
        print('You received an 8')
    if c7 == 9:
        print('You received a 9')
    if c7 == 10:
        print('You received a 10')
    if c7 == 11:
        print('You received a Jack')
    if c7 == 12:
        print('You received a Queen')
    if c7 == 13:
        print('You received a King')
    playercount = int((c1 + c3 + c5 + c7))
    if (c1 + c3 + c5 + c7) > 21:
        bust()
    anothercard()
    resp = input()
    if resp == 'h':
        hit3()
    if resp == 's':
        stand()
    if resp == 'e':
        endgame()
def hit1():
    global c1, c2, c3, c4, c5
    global bet
    import random
    global playercount
    low = (1)
    high =(14)
    ran_number5 = random.uniform(low, high)
    c5 = (int(ran_number5))
    if c5 == 1:
        print('You received an Ace')
    if c5 == 2:
        print('You received a 2')
    if c5 == 3:
        print('You received a 3')
    if c5 == 4:
        print('You received a 4')
    if c5 == 5:
        print('You received a 5')
    if c5 == 6:
        print('You received a 6')
    if c5 == 7:
        print('You received a 7')
    if c5 == 8:
        print('You received an 8')
    if c5 == 9:
        print('You received a 9')
    if c5 == 10:
        print('You received a 10')
    if c5 == 11:
        print('You received a Jack')
    if c5 == 12:
        print('You received a Queen')
    if c5 == 13:
        print('You received a King')
    playercount = int((c1 + c3 + c5))
    if (c1 + c3 + c5) > 21:
        bust()
    anothercard()
    resp = input()
    if resp == 'h':
        hit2()
    if resp == 's':
        stand()
    if resp == 'e':
        endgame()
def wrong():
    global chips
    global bet
    print('You did not enter the correct amount of chips for that bet.')
    print('Note that the high is low is 100 and the high is 10,000.')
    bet = int(input('Please enter your bet.'))
def lose():
    space()
    import random
    low = (1)
    high = (5)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Looks like the house wins this one.')
    if rr == 2:
        print('Dealer: Oh, tough luck.')
    if rr == 3:
        print('Dealer: Dealer wins this one.')
    if rr == 4:
        print('Dealer: Ah, dealer wins.')
    play()
def reveal():
    space()
    global c1, c2, c3, c4, c5, c6
    import random
    low = (1)
    high = (3)
    ran_number = random.uniform(low, high)
    rr = (int(ran_number))
    if rr == 1:
        print('Dealer: Lets see how this turns out.')
    if rr == 2:
        print('Dealer: Lets show my card here.')
    if c4 == 1:
        print('The Dealer revealed an Ace')
    if c4 == 2:
        print('The Dealer revealed a 2')
    if c4 == 3:
        print('The Dealer revealed a 3')
    if c4 == 4:
        print('The Dealer revealed a 4')
    if c4 == 5:
        print('The Dealer revealed a 5')
    if c4 == 6:
        print('The Dealer revealed a 6')
    if c4 == 7:
        print('The Dealer revealed a 7')
    if c4 == 8:
        print('The Dealer revealed an 8')
    if c4 == 9:
        print('The Dealer revealed a 9')
    if c4 == 10:
        print('The Dealer revealed a 10')
    if c4 == 11:
        print('The Dealer revealed a Jack')
    if c4 == 12:
        print('The Dealer revealed a Queen')
    if c4 == 13:
        print('The Dealer revealed a King')
def stand4():
    global chips
    global c1, c2, c3, c4, c5, c6, c8, c10, c12
    global bet
    global playercount
    space()
    if c12 == 1:
        print('The Dealer received an Ace')
    if c12 == 2:
        print('The Dealer received a 2')
    if c12 == 3:
        print('The Dealer received a 3')
    if c12 == 4:
        print('The Dealer received a 4')
    if c12 == 5:
        print('The Dealer received a 5')
    if c12 == 6:
        print('The Dealer received a 6')
    if c12 == 7:
        print('The Dealer received a 7')
    if c12 == 8:
        print('The Dealer received an 8')
    if c12 == 9:
        print('The Dealer received a 9')
    if c12 == 10:
        print('The Dealer received a 10')
    if c12 == 11:
        print('The Dealer received a Jack')
    if c12 == 12:
        print('The Dealer received a Queen')
    if c12 == 13:
        print('The Dealer received a King')
    if (c2 + c4 + c6 + c8 + c10 + c12) > 21:
        winner()
    if (c2 + c4 + c6 + c8 + c10 + c12) < int(playercount):
        winner()
    if (c2 + c4 + c6 + c8 + c10 + c12) > int(playercount):
        lose()
    if (c2 + c4 + c6 + c8 + c10 + c12) <= 17 and (c2 + c4 + c6 + c8 + c10 + c12) < int(playercount):
        print('Man, I didnt think the dealer would get this lucky to still be using cards. I will let you win.')
        winner()
def stand3():
    global chips
    global c1, c2, c3, c4, c5, c6, c8, c10
    global bet
    global playercount
    space()
    if c10 == 1:
        print('The Dealer received an Ace')
    if c10 == 2:
        print('The Dealer received a 2')
    if c10 == 3:
        print('The Dealer received a 3')
    if c10 == 4:
        print('The Dealer received a 4')
    if c10 == 5:
        print('The Dealer received a 5')
    if c10 == 6:
        print('The Dealer received a 6')
    if c10 == 7:
        print('The Dealer received a 7')
    if c10 == 8:
        print('The Dealer received an 8')
    if c10 == 9:
        print('The Dealer received a 9')
    if c10 == 10:
        print('The Dealer received a 10')
    if c10 == 11:
        print('The Dealer received a Jack')
    if c10 == 12:
        print('The Dealer received a Queen')
    if c10 == 13:
        print('The Dealer received a King')
    if (c2 + c4 + c6 + c8 + c10) > 21:
        winner()
    if (c2 + c4 + c6 + c8 + c10) < int(playercount):
        winner()
    if (c2 + c4 + c6 + c8 + c10) > int(playercount):
        lose()
    if (c2 + c4 + c6 + c8 + c10) <= 17 and (c2 + c4 + c6 + c8 + c10) < int(playercount):
        stand4()
def stand2():
    global chips
    global c1, c2, c3, c4, c5, c6, c8
    global bet
    global playercount
    space()
    if c8 == 1:
        print('The Dealer received an Ace')
    if c8 == 2:
        print('The Dealer received a 2')
    if c8 == 3:
        print('The Dealer received a 3')
    if c8 == 4:
        print('The Dealer received a 4')
    if c8 == 5:
        print('The Dealer received a 5')
    if c8 == 6:
        print('The Dealer received a 6')
    if c8 == 7:
        print('The Dealer received a 7')
    if c8 == 8:
        print('The Dealer received an 8')
    if c8 == 9:
        print('The Dealer received a 9')
    if c8 == 10:
        print('The Dealer received a 10')
    if c8 == 11:
        print('The Dealer received a Jack')
    if c8 == 12:
        print('The Dealer received a Queen')
    if c8 == 13:
        print('The Dealer received a King')
    if (c2 + c4 + c6 + c8) > 21:
        winner()
    if (c2 + c4 + c6 + c8) < int(playercount):
        winner()
    if (c2 + c4 + c6 + c8) > int(playercount):
        lose()
    if (c2 + c4 + c6 + c8) <= 17 and (c2 + c4 + c6 + c8) < int(playercount):
        stand3()
def stand():
    global chips
    global c1, c2, c3, c4, c5, c6
    global bet
    global playercount
    space()
    reveal()
    if (c2 + c4) > (c1 + c3):
        lose()
    print('The dealer begins to place another card.')
    if c6 == 1:
        print('The Dealer received an Ace')
    if c6 == 2:
        print('The Dealer received a 2')
    if c6 == 3:
        print('The Dealer received a 3')
    if c6 == 4:
        print('The Dealer received a 4')
    if c6 == 5:
        print('The Dealer received a 5')
    if c6 == 6:
        print('The Dealer received a 6')
    if c6 == 7:
        print('The Dealer received a 7')
    if c6 == 8:
        print('The Dealer received an 8')
    if c6 == 9:
        print('The Dealer received a 9')
    if c6 == 10:
        print('The Dealer received a 10')
    if c6 == 11:
        print('The Dealer received a Jack')
    if c6 == 12:
        print('The Dealer received a Queen')
    if c6 == 13:
        print('The Dealer received a King')
    if (c2 + c4 + c6) > 21:
        winner()
    if (c2 + c4 + c6) < int(playercount):
        winner()
    if (c2 + c4 + c6) > int(playercount):
        lose()
    if (c2 + c4 + c6) <= 17 and (c2 + c4 + c6) < int(playercount):
        stand2()
def play():
    global chips
    global c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12
    global bet
    space()
    import random
    low = (1)
    high = (14)
    ran_number = random.uniform(low, high)
    ran_number2 = random.uniform(low,high)
    ran_number3 = random.uniform(low, high)
    ran_number4 = random.uniform(low, high)
    ran_number5 = random.uniform(low, high)
    ran_number6 = random.uniform(low, high)
    ran_number7 = random.uniform(low, high)
    ran_number8 = random.uniform(low, high)
    ran_number9 = random.uniform(low, high)
    ran_number10 = random.uniform(low, high)
    ran_number11= random.uniform(low, high)
    ran_number12= random.uniform(low, high)
    c1 = (int(ran_number))
    c2 = (int(ran_number2))
    c3 = (int(ran_number3))
    c4 = (int(ran_number4))
    c5 = (int(ran_number5))
    c6 = (int(ran_number6))
    c7 = (int(ran_number7))
    c8 = (int(ran_number8))
    c9 = (int(ran_number9))
    c10 = (int(ran_number10))
    c11 = (int(ran_number11))
    c12 = (int(ran_number12))
    placebet()
    bet = int(input())
    while bet > chips:
        wrong()
    if bet < 100 or bet > 10000:
        wrong()
    greeting()
    chips = int((chips - bet))
    space()
    nomorebets()
    cards1()
    space()
    anothercard()
    resp = input()
    if resp == 'h':
        hit1()
    if resp == 's':
        stand()
    if resp == 'e':
        endgame()
def blackjack():
    space()
    play()
def main():
    space()
    print('       Main Menu')
    print('$--$--$--$--$--$--$--$')
    print('1. Game Rules')
    print('2. Scoreboard')
    print('3. Play Game')
    print('4. Quit')
    mm = input()
    if mm == '1':
        gamerules()
    if mm == '2':
        scoreboard()
    if mm == '3':
        blackjack()
    if mm == '4':
        quitgame()
# Header
print('Welcome to Flux Casino')
space()
global chips
global playercount
playercount = int(0)
chips = int(5000)
main()