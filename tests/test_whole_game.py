import pytest
import pexpect
from pexpect import spawn

# pytest test_program.py

def test_program():
    child = pexpect.spawn('python game.py')

    for num in range(1, 14):
        child.expect('.*Enter your dice roll, 5,4,3,2,1:\r\n')
        child.sendline("1,1,1,1,1")
        child.expect('.*Choose the result you wish to add to your scoreboard, type a number:\r\n')
        child.sendline(str(num))
    
    assert child.isalive() == False
    assert child.exitstatus == 0
