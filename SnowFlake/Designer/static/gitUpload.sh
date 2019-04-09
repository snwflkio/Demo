#!/bin/bash

#mkdir -p cd ~/Dropbox/Snowflake/snwflkio.github.io/Creations/$1;
cd ../../../../snwflkio.github.io/;

git add .;
git commit -m "$2";
git push origin master;
