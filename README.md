# brainstorm

[![build](https://github.com/znhv/oasis/actions/workflows/build.yml/badge.svg)](https://github.com/znhv/oasis/actions/workflows/build.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/2bb66c194e439ea25c08/maintainability)](https://codeclimate.com/github/notabu/python-project-lvl1/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/2bb66c194e439ea25c08/test_coverage)](https://codeclimate.com/github/notabu/python-project-lvl1/test_coverage) 


A set of five console games along the lines of popular mobile brain-pumping apps. Each game asks questions that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end the game and prompt you to play it again.

## Prerequisite
#### [Poetry](https://python-poetry.org)

osx / linux / bashonwindows install instructions
```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

windows powershell install instructions
```shell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

## Installation

Clone the repo and install packages
```sh
git clone https://github.com/znhv/brainstorm.git && cd brainstorm && make install
```
   
## Play
```shell
$ brainstorm 
Welcome to the BRAINSTORM! 

? Menu  (Use arrow keys)
 ❯ Play
   Stats
   Exit
```

## [List of games](docs/games.md)

## License
[MIT](https://github.com/znhv/brain-games/blob/main/LICENSE)