# Yahtzee Game/ Scorer

- Github project board
- Github workflow
- Github branches
- Test Driven Development (TDD)

The code uses a github workflow, everytime a pull request is made a series of unit tests are automatically run on the code via pytest to ensure the core code is always working. I used TDD to develop the code - *see image below*.

I used a github project board and broke work into small and achievable pieces and I asked for support around TDD from a mentor for this project, as TDD was new to me and I was using [VS Studio website](https://code.visualstudio.com/docs/python/testing) to support my learning.

One area of learning here was BDD vs TDD. The design process is more about behaviour driven development(BDD) and the building and coding of the core score calculator was more about the test driven development(TDD).

### Project Plan
The plan here is to have Yahtzee in 2 forms:
- as a command line game, where the computer rolls the dice for a max of 6 players and track the score
- as a scorer that can be used to score individual dice rolls

===
# TDD
A rewardingly green screenshot to show how I developed using unittests in pytest.
These commit codes mark a point where I clearly show TDD in action - *game_dev d2588ae* and *game_dev 8955bbb*. There are examples throughout my work in this project but this one was an intentional capture to show my process of using TDD on a branch called *game_dev*.

![Image - Screenshot](./images/tdd_yahtzee.jpg)