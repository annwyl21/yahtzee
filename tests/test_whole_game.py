import pytest
import pexpect

# pytest test_whole_game.py
# Integration testing - testing multiple components of an application together to ensure they work correctly as a group
# NEEDS TO BE RUN USING THE UBUNTU TERMINAL BECAUSE SPAWN DOESN'T WORK WITH WINDOWS

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

