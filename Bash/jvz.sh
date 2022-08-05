#!/bin/bash

# ----------------------
# Author : Felix Filipi
# ----------------------

# Script start here
if [ ${#} -eq 0 ]
then
  cd ~/Project/
fi

case ${1} in
  -g)
    if [[ ("${2}" == "C" ) || ("${2}" == "c") ]]
    then
      cd ~/Project/C_project

    elif [[ ("${2}" == "RN") || ("${2}" == "rn") ]]
    then
      cd ~/Project/RN_project

    elif [[ ("${2}" == "WEB") || ("${2}" == "web") ]]
    then
      cd ~/Project/Web_project

    else
      echo "$0 : usage [C][RN][WEB]"

    fi
    ;; 
  -b)
    cd ~/
    ;;
  -set)
    firefox
    tmux
    ;;
  -net)
    ping 8.8.8.8
esac
