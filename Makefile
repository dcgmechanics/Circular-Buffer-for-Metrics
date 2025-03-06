.PHONY: clean test install develop

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

test:
	python -m unittest discover tests

install:
	pip install .

develop:
	pip install -e .

build:
	python setup.py sdist bdist_wheel 