[![Python application test with Github Actions](https://github.com/ThanatPay/pytest-tips/actions/workflows/test-ci.yml/badge.svg)](https://github.com/ThanatPay/pytest-tips/actions/workflows/test-ci.yml)
# pytest-tips
A primer of pytest

#### Start virtual environment
Create virtual environment into an invisible directory inside your home directory that it's not going to be accidentally pushed into your GitHub repo.
```
virtualenv ~/.venv
```
activate virtual environment
```
source ~/.venv/bin/activate
```
But when you change bash terminal it out of virtual environment. You can fix this by set default in bashrc
`vim ~/.bashrc`

#### Test
create Makefile and requirement to set what do you need
`source Makefile` to set command for make
- install : `pip install --upgrade pip && pip install -r requirements.txt`
- pytest  : check conditions for test case
- pylint  : check error and warning
- black   : check format of syntax

`source requirements.txt` to set library that you need
- after you run `make install` to install requirements library, you can check version of library to set requirements again for fix version by `pip freeze | less`

you must be create build system by GitHub Actions to allow double check before drive into others environment or cloud platform
