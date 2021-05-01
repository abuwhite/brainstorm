# Brain Games
[![Actions Status](https://github.com/notabu/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/notabu/python-project-lvl1/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/2bb66c194e439ea25c08/maintainability)](https://codeclimate.com/github/notabu/python-project-lvl1/maintainability) [![Python CI](https://github.com/notabu/python-project-lvl1/actions/workflows/pyci.yml/badge.svg)](https://github.com/notabu/python-project-lvl1/actions/workflows/pyci.yml)

A set of five console games built on the principle of popular mobile applications for brain pumping.
Each game asks questions that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end the game and offer to play it again.

### Games
+ Calculator. Arithmetic expressions to be evaluated.
+ Progression. Search for missing numbers in a sequence of numbers.
+ Determining an even number.
+ Determining the greatest common divisor.
+ Definition of a prime number.

## Example:

### Progression
```$ brain-progression
Welcome to the Brain Game!
What number is missing in this progression?
May I have your name? Roman
Hello, Roman!
Question: 14 .. 18 20 22 24 26 28
Your answer: 16 # Пользователь вводит ответ
Correct!
Question: 5 6 7 8 9 .. 11 12
Your answer: 10 # Пользователь вводит ответ
Correct!
Question: 12 15 18 21 .. 27 30 33
Your answer: 24 # Пользователь вводит ответ
Correct!
Congratulations, Roman!
```

## Project setup
Use `make run` to build and run docker containers with application itself and mongodb instance
