# This file is part of Oasis
# https://github.com/znhv/oasis

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2021 Boris Zhenikhov

POETRY_RELEASE := $$(sed -n -E "s/__version__ = '(.+)'/\1/p" oasis/__version__.py)

install:
	@poetry install
	@poetry build
	python3 -m pip install dist/*.whl --force-reinstall

clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

format: clean
	@poetry run black oasis/ tests/

test:
	make lint
	make pytest
	make pytest-cov

lint:
	poetry run flake8 oasis

pytest:
	poetry run pytest oasis tests/

cov-check:
	poetry run pytest --cov=oasis tests/

pytest-cov:
	@poetry run pytest --cov=oasis --cov-config .coveragerc tests/ -sq --cov-report xml

build: test
	@poetry build

oasis:
	poetry run oasis