install:
	poetry install
	make build
	python3 -m pip install dist/*.whl --force-reinstall

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime