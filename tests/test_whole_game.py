import pytest
import pexpect
from pexpect import spawn

# pytest test_program.py

def test_program():
    child = pexpect.spawn('python game.py')
    # Roll 1
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('1')
    # Roll 2
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('2')
    # Roll 3
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('3')
    # Roll 4
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('4')
    # Roll 5
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('5')
    # Roll 6
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('6')
    # Roll 7
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('7')
    # Roll 8
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('8')
    # Roll 9
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('9')
    # Roll 10
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('10')
    # Roll 11
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('11')
    # Roll 12
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('12')
    # Roll 13
    child.expect("Enter your dice roll, 5,4,3,2,1:\n")
    child.sendline("1,1,1,2,3")
    child.expect('Choose the result you wish to add to your scoreboard, type a number:\n')
    child.sendline('13')
    assert child.isalive() == False
    assert child.exitstatus == 0
