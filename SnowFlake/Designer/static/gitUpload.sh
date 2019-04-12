#!/bin/bash

#mkdir -p cd ~/Dropbox/Snowflake/snwflkio.github.io/Creations/$1;
cd ../../snwflkio.github.io/;

git add .;

echo "\"${@:2}\"";
args=${@:2}
git commit -m "'$args'";
git push -u origin master;
