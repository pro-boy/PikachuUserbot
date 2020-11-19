#!/bin/bash
# © @ItzSjdude, Made for Pikabot
_logo() {
    echo '╔═╦╦╗───╔╗──╔╗'
    echo '║╬╠╣╠╦═╗║╚╦═╣╚╗'
    echo '║╔╣║═╣╬╚╣╬║╬║╔╣'
    echo '╚╝╚╩╩╩══╩═╩═╩═╝'
}

_cleanup() {
    echo 'Cleaning up Pikabot'
    rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_source() {
    echo 'Getting Source Ready' 
    git clone -b Beta https://github.com/ItzSjDude/PikachuUserbot ./
}

_upgradePip() {
    echo '••• Updating Pip •••' 
    pip3 install -U pip &> /dev/null
    echo '••• Updated Pip •••'
}

_insReq() {
    echo '••• Installing Requirements •••'
    pip install -r requirements.txt
    echo '••• Installed Requirements •••'
}

start() {
    _logo
    _cleanup
    _source
    _upgradePip
    _insReq
    mkdir ./pikabot/main_plugs
    python3 -m pikabot
}
