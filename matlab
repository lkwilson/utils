#!/bin/bash

bin=/Applications/MATLAB_R2017b.app/bin/matlab
args='-nodisplay -nojvm -nosplash'

usage() {
    echo "Bad opt: $OPTARG"
    echo '  -h to display this'
    echo '  -d to enable display'
    echo '  -i to open application'
    exit 1
}

while getopts ":di" opt; do
    case $opt in
      d) args='-nodesktop -nosplash' ;;
      i) args='' ;;
      h) usage ;;
      \?) usage ;;
    esac
done

$bin $args
