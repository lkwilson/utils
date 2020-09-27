#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    sess=main
else
    sess="$1"
fi

tmux a -t "$sess" || tmux new -s "$sess"
