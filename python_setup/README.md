# Install pyenv
```curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash```

# Add to end of .bashrc (depends on which bash)
```
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

# Restart terminal

# Install a python version
`pyenv install 3.9`

# Setup a virtualenv in a directory
```
NAME=my_python_service
mkdir ~/${NAME}
cd ~/${NAME}
pyenv virtualenv 3.9 ${NAME}_env
pyenv local ${NAME}_env # Must be inside the target directory.
```
