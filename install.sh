#! /bin/bash

SRC_DIR="${PWD}/$(dirname $0)"

ln -sf $SRC_DIR/stopwatch.py $HOME/.local/bin/stopwatch
ln -sf $SRC_DIR/countdown.py $HOME/.local/bin/countdown
