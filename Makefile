install:
	poetry install
	make build
	python3 -m pip install dist/*.whl --force-reinstall

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 oasis

oasis:
	poetry run oasis