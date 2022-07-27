#!/bin/sh

url="https://artgare.com"
download_dir="$HOME/Downloads"

download() {
    aria2c --dir="${download_dir}" "$1"
}

main() {
    resp=$(curl -s "${url}" -A "uwu" | grep -Eo "https://artgare.com/free-3d-model/[a-zA-Z0-9%-]*/" | uniq)
    selected=$(printf "%s\n" "$resp" | fzf)
    req=$(curl -s "$selected" | grep -Eo "https://cdn.discordapp.com/attachments/[0-9]{18}/[0-9]{18}/[a-zA-Z0-9_-]*.zip")
    download "$req"
}

main
