#!/bin/bash

mkdir -p ../../../../snwflkio.github.io/Creations/$1;
cd ../../../../snwflkio.github./Creations/$1;
echo "poop" >> ho.txt

git add .;
git commit -m "$2";
git push origin master;
