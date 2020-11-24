#!/bin/bash
# © @ItzSjdude, Made for Pikabot
_logo() {
    echo '
    ╔═╦╦╗───╔╗──╔╗
    ║╬╠╣╠╦═╗║╚╦═╣╚╗
    ║╔╣║═╣╬╚╣╬║╬║╔╣
    ╚╝╚╩╩╩══╩═╩═╩═╝
    '
}

_cleanup() {
    echo 'Cleaning up Pikabot'
    rm -rf ./plugins && rm -rf ./* && rm -rf ./.gitignore && rm -rf ./.git
} 

_source() {
    echo 'Getting Source Ready' 
    git clone -b Beta https://github.com/ItzSjDude/PikachuUserbot ./
    mkdir ./plugins && ./Temp
    git clone https://github.com/ItzSjDude/PikaBotPlugins ./Temp
    cp ./Temp/plugins/*.py ./plugins && cp ./Temp/plugins/resources/*.py ./pikabot
    rm -rf ./Temp
}

_upgradePip() {
    echo '••• Updating Pip •••' 
    pip3 install -U pip &> /dev/null
    echo '••• Updated Pip •••'
}

_insReq() {
    echo '••• Installing Requirements •••'
    pip install -r requirements.txt &> /dev/null
    echo '••• Installed Requirements •••'
}

start() {
    _logo
    _cleanup
    _source
    _upgradePip
    mkdir ./pikabot/main_plugs
    python3 -m pikabot
}
