#!/bin/bash

. init/Deps.sh 

echo 'Cleaning up 'Pikabot'
rm -rf ./ && rm -rf ./.gitignore && rm -rf ./.git

echo 'Getting Source Ready' 
git clone -b Beta https://github.com/ItzSjDude/PikachuUserbot ./

