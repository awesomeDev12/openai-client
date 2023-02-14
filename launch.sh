#!/bin/bash

#echo Hello >> /home/darklord/Desktop/openai-client/log.txt
#python /home/darklord/Desktop/openai-client/main.py
#python main.py


#export OPENAI_CLIENT_DIR=/home/darklord/Desktop/openai-client
export OPENAI_CLIENT_DIR=/home/${USER}/Desktop/openai-client

echo Hello >> $OPENAI_CLIENT_DIR/log.txt
python $OPENAI_CLIENT_DIR/main.py
