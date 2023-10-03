# [Yahtzee Scorer](https://annwyl21.github.io/yahtzee_scorer/yahtzeedemo.html) deployed to replit

- Test Driven Development (TDD) - Pytest and Pexpect
- Using the debugger to problem solve
- Github project, workflow & branches

The complex rules of Yahtzee along with the challenge of tracking the score through the game makes this an ideal challenge for a junior developer like me. 
1. The first step was to write a score calculator and create a game against a computer adversary, which I have now deployed to replit. 
2. The next evolution for this game will be to replace the computer player with family players so that I can use my app to calculate and track scores during a family game.

### A Command Line Scoring Program:
- The **calculator class** can be used as a scorer that can be used to score individual dice rolls

- The **scoreboard class** contains methods that can be called to produce a scoreboard during the game and an overall score at the end of a game.

## Development Overview

This repository represents use of **GitHub workflows** to ensure the continuous quality of our code. Every time a pull request is initiated, a batch of unit tests is executed automatically on the proposed code. This is achieved using `pytest`, a robust Python testing tool, which ensures that the core functionality of the code remains intact at all times. 

My development approach leaned heavily on **Test-Driven Development (TDD)**. This methodology emphasizes writing tests before the actual code. As illustrated in the image below, my TDD workflow involved using `pytest` for unit testing and `Pexpect` for integration testing. This project has also really given me an opportunity to use the **debugger** to debug tests and code. Use of the debugger helped me to quickly and easily spot a late night error in my own tests.

To manage my tasks effectively, I utilized a **GitHub project board**, splitting my objectives into manageable, achievable segments. This practice was instrumental in keeping the project on track and my goals clear.

===
# TDD
A rewardingly green screenshot to show how I developed using unit tests in pytest.

![Image - Screenshot](./images/tdd_yahtzee.jpg)
