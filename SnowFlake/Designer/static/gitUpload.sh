#!/bin/bash

mkdir -p ../../../../snwflkio.github.io/Creations/$1;
git add .;
git commit -m "$2";
git push origin master;