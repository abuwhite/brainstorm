# brainstorm

[![build](https://github.com/znhv/oasis/actions/workflows/build.yml/badge.svg)](https://github.com/znhv/oasis/actions/workflows/build.yml) [![Maintainability](https://api.codeclimate.com/v1/badges/2bb66c194e439ea25c08/maintainability)](https://codeclimate.com/github/notabu/python-project-lvl1/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/2bb66c194e439ea25c08/test_coverage)](https://codeclimate.com/github/notabu/python-project-lvl1/test_coverage) 


[A set of console games](docs/games.md) by analogy with popular mobile applications for brain pumping. In each game, questions are asked that must be answered correctly. One point is awarded for each correct answer. After three answers, the game is considered completed.

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

## License
[MIT](https://github.com/znhv/brain-games/blob/main/LICENSE)