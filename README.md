[![Python application test with Github Actions](https://github.com/ThanatPay/pytest-tips/actions/workflows/test-ci.yml/badge.svg)](https://github.com/ThanatPay/pytest-tips/actions/workflows/test-ci.yml)
# pytest-tips
A primer of pytest

## Start virtual environment
Create virtual environment into an invisible directory inside your home directory that it's not going to be accidentally pushed into your GitHub repo
```
virtualenv ~/.venv
```
activate virtual environment
```
source ~/.venv/bin/activate
```
But when you change bash terminal it out of virtual environment. You can fix this by set default in bashrc
`vim ~/.bashrc`

## Test
create Makefile `source Makefile` to set command for make
- install : `pip install --upgrade pip && pip install -r requirements.txt`
- pytest  : check conditions for test case
    - Simple version: `python -m pytest -vv test_hello.py`
    - Adding Code Coverage: `python -m pytest -vv --cov=hello test_hello.py`
    - Adding Jupyter Notebook testing with nbval: `python -m pytest --nbval notebook.ipynb`
    - Adding debug code with PDB: `python -m pytest -vv --pdb`
    - Test only function: `python -m pytest -vv tests test_greeting.py::test_my_name4`
- pylint  : check error and warning
    - Simple version:`pylint --disable=R,C *.py`
- black   : check format of syntax
    - Simple version: `black *.py`

create requirement to set what do you need `source requirements.txt` to set library that you need
- after you run `make install` to install requirements library, you can check version of library `pip freeze | less` to set requirements again for fix version

## CI system with pytest
you must be create build system (GitHub Actions, AWS codebuild) to allow double check before drive into others environment or cloud platform.