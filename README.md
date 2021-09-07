# Brain Games

[![Python CI](https://github.com/notabu/python-project-lvl1/actions/workflows/pyci.yml/badge.svg)](https://github.com/notabu/python-project-lvl1/actions/workflows/pyci.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/2bb66c194e439ea25c08/maintainability)](https://codeclimate.com/github/notabu/python-project-lvl1/maintainability) 


A set of five console games along the lines of popular mobile brain-pumping apps. Each game asks questions that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end the game and prompt you to play it again.


## Installation

Clone the repo and install packages
```sh
git clone https://github.com/znhv/brain-games.git

cd brain-games
   
make install
```
   
## Usage

**Brain Even.**

The user is presented And he has to answer yes if the number is even, or no if it is odd.
```shell
$ brain-even

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!
```

**Brain Calc.**

The user is shown a random mathematical expression, such as 35 + 16, which must be calculated and write down the correct answer.
```shell
$ brain-calc

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!
```

**Brain Gcd.**

The user is shown two random numbers, e.g., 25 50. The user must calculate and enter the greatest common divisor of these numbers.
```shell
$ brain-gcd

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!               
```

**Brain Progression.**

The user is shown a series of numbers that form an arithmetic progression, replacing any of the numbers with two dots. The player must determine this number.
```shell
$ brain-progression

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
```


**Brain Prime.**

The user is shown a random number. The player must determine if it is a prime number.
```shell
$ brain-prime
Welcome to the Brain Games!
May I have your name? Tirion
Hello, Tirion!
Answer 'yes' if given number is prime. Otherwise answer 'no'.
Question: 3
Your answer: yes
Correct!
Question: 5
Your answer: yes
Correct!
Question: 6
Your answer: no
Correct!
Congratulations, Tirion!      
```

## License
[MIT](https://github.com/znhv/brain-games/blob/main/LICENSE)