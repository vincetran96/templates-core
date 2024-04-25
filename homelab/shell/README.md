# zsh
## Install
- `apt install zsh`
- Make `zsh` default: https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH#install-and-set-up-zsh-as-default
## autosuggestion
- https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md#manual-git-clone
## .zshrc
```
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# thefuck
eval $(thefuck --alias)

# command alias
alias cl='clear'
alias gs='git status'
alias gl='git log'
alias gfp='git fetch && git pull'
alias gc='git checkout'
alias gcb='git checkout -b'
alias gstash='git stash'
alias dps='docker ps'
```
