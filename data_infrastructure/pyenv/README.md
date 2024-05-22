## Install pyenv
- ```curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash```
- [Packages to build pyenv](https://stackoverflow.com/questions/60775172/pyenvs-python-is-missing-bzip2-module)

## Add to end of .bashrc (depends on which bash)
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

## Restart terminal

## Install a python version
`pyenv install 3.9`

## Setup a virtualenv in a directory
```
NAME=my_python_service
mkdir ~/${NAME}
cd ~/${NAME}
pyenv virtualenv 3.9 ${NAME}_env
pyenv local ${NAME}_env # Must be inside the target directory.
```
