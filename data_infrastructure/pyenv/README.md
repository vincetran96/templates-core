# Setup pyenv
## Install
- [pyenv build environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)
- ```curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash```
## Add to end of .bashrc (depends on which shell)
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

# Install a python version
`pyenv install 3.9`
## Setup a virtualenv in a directory
```
NAME=my_python_service
mkdir ~/${NAME}
cd ~/${NAME}
pyenv virtualenv 3.9 ${NAME}_env
pyenv local ${NAME}_env # Must be inside the target directory.
```
