install:
	poetry install
	make build
	python3 -m pip install dist/*.whl --force-reinstall

build:
	rm -rf dist/*
	poetry build

lint:
	poetry run flake8 oasis

test:
	poetry run pytest oasis tests/

test-cov:
	poetry run pytest --cov=oasis tests/ --cov-report xml

oasis:
	poetry run oasis