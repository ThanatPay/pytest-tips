install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting tests
	python -m pytest --nbval notebook.ipynb

debug:
	# Debugger in invoked
	python -m pytest -vv --pdb

one-test:
	# test only function test_my_name4
	python -m pytest -vv tests/test_greeting.py::test_my_name4

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test format