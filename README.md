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
