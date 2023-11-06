#!/bin/bash
#!/usr/bin/python python
#!/usr/bin/git git
#!/usr/bin/gnome-terminal gnome-terminal

killall python3

sleep 1

cd /home/user/Downloads/program_from_git/test_repository

git pull

echo "Program restarting" >> /home/user/Downloads/program_from_git/state.log
export DSIPLAY=:2

