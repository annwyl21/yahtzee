import pytest
import pexpect

# pytest test_whole_game.py
# Integration testing - testing multiple components of an application together to ensure they work correctly as a group
# NEEDS TO BE RUN USING THE UBUNTU TERMINAL BECAUSE SPAWN PREFERS UNIX-LIKE ENVIRONMENTS

def test_program():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("1,1,1,1,1")
        child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
        child.sendline(str(num))
    
    child.expect('Goodbye\r\n')

    # assert child.isalive() == False
    # assert child.exitstatus == 0

def test_program_with_invalid_dice_roll():
    child = pexpect.spawn('python game.py')
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("1,1,1,1,1,1")
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')

def test_grand_score():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("1,3,3,5,5")
        child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
        child.sendline(str(num))
    
    child.expect('.*34')

def test_grand_score_with_yahtzee_roll():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("1,1,1,1,1")
        child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
        child.sendline(str(num))
    
    child.expect('.*360') #work out the score

def test_grand_score_with_larger_score():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("6,6,6,6,6")
        child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
        child.sendline(str(num))
    
    child.expect('.*410') #work out the score 

def test_score_max_possible(): #perfect hands every time
    child = pexpect.spawn('python game.py')

    # roll 1
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("1,1,1,1,1")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('1')
    # roll 2
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("2,2,2,2,2")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('2')
    # roll 3
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("3,3,3,3,3")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('3')
    # roll 4
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("4,4,4,4,4")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('4')
    # roll 5
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("5,5,5,5,5")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('5')
    # roll 6
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("6,6,6,6,6")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('6')
    # roll 7 - 3 of a kind
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("6,6,6,1,2")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('7')
    # roll 8 - 4 of a kind
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("6,6,6,6,2")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('8')
    # roll 9 - full house
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("6,6,6,2,2")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('9')
    # roll 10 - sm-straight
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("5,6,3,1,4")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('10')
    # roll 11 - lg-straight
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("5,6,3,2,4")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('11')
    # roll 12 - chance
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("6,6,6,6,6")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('12')
    # roll 13 - yahtzee
    child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
    child.sendline("6,6,6,6,6")
    child.expect('.*Type a number to choose the result you wish to add to your scoreboard:\r\n')
    child.sendline('13')

    child.expect('.*657')
