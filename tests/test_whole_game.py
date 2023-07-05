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
        child.expect('.*Choose the result you wish to add to your scoreboard, type a number:\r\n')
        child.sendline(str(num))
    
    child.expect('Goodbye\r\n')

    # assert child.isalive() == False
    # assert child.exitstatus == 0

def test_grand_score():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("1,3,3,5,5")
        child.expect('.*Choose the result you wish to add to your scoreboard, type a number:\r\n')
        child.sendline(str(num))
    
    child.expect('.*34')

def test_grand_score_with_yahtzee_roll():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("1,1,1,1,1")
        child.expect('.*Choose the result you wish to add to your scoreboard, type a number:\r\n')
        child.sendline(str(num))
    
    child.expect('.*160') #work out the score

def test_grand_score_with_larger_score():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("6,6,6,6,6")
        child.expect('.*Choose the result you wish to add to your scoreboard, type a number:\r\n')
        child.sendline(str(num))
    
    child.expect('.*210') #work out the score 
