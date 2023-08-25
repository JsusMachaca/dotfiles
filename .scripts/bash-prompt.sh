#!/bin/bash
#
# DESCRIPTION:
#
#   Set the bash prompt according to:
#    * the active virtualenv
#    * the branch of the current git/mercurial repository
#    * the return value of the previous command
#    * the fact you just came from Windows and are used to having newlines in
#            RED="\[\033[0;31m\]"

YELLOW="\[\033[1;33m\]"
GREEN="\[\033[0;32m\]"
BLUE="\[\033[1;34m\]"
PURPLE="\[\033[0;35m\]"
LIGHT_RED="\[\033[1;31m\]"
LIGHT_GREEN="\[\033[1;32m\]"
WHITE="\[\033[1;37m\]"
LIGHT_GRAY="\[\033[0;37m\]"
COLOR_NONE="\[\e[0m\]"

#      your prompts.
#
# USAGE:
#
#   1. Save this file as ~/.bash_prompt
#   2. Add the following line to the end of your ~/.bashrc or ~/.bash_profile:
#        . ~/.bash_prompt
#
# LINEAGE:
#
#   Based on work by woods
#
#   https://gist.github.com/31967
# Determine active Python virtualenv details.
function set_virtualenv () {
  if test -z "$VIRTUAL_ENV" ; then
      PYTHON_VIRTUALENV=""
  else
      PYTHON_VIRTUALENV=" |  `basename \"$VIRTUAL_ENV\"`"
  fi
}

# Set the full bash prompt.
function set_bash_prompt () {
  # Set the PROMPT_SYMBOL variable. We do this first so we don't lose the
  # return value of the last command.

  # Set the PYTHON_VIRTUALENV variable.
  set_virtualenv

  # Set the BRANCH variable.

  # Set the bash prompt variable.
#  PS1="
#${PYTHON_VIRTUALENV}${GREEN}\u@\h${COLOR_NONE}:${YELLOW}\w${COLOR_NONE}${BRANCH}
#${PROMPT_SYMBOL} "

PS1='┌─[\[\e[38;5;221m\]\u\[\e[0m\]   \[\e[38;5;39m\]\h \[\e[0m\]| \[\e[38;5;30m\]\W\[\e[0m\]${PYTHON_VIRTUALENV}\[\e[0m\]] \[\033[33m\]$(__git_ps1 "  %s") \n└──\[\e[38;5;159;1m\] '
}
# Tell bash to execute this function just before displaying its prompt.
PROMPT_COMMAND=set_bash_prompt
