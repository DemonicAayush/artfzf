#!/usr/bin/env bash

url="https://artgare.com"
download_dir="$HOME/Downloads"

download() {
    aria2c --dir="${download_dir}" "$1"
}

main() {
    resp=$(curl -s "$1" -A "uwu" | grep -Eo "https://artgare.com/free-3d-model/[a-zA-Z0-9%-]*/" | uniq)
    selected=$(printf "%s\n" "$resp" | fzf)
    
    [[ -z "$selected" ]] && printf "%s\n" "[!] Nothing to download" && exit 1
    
    req=$(curl -s "$selected" | grep -Eo "https://cdn.discordapp.com/attachments/[0-9]{18}/[0-9]{18}/[a-zA-Z0-9_-]*.zip")
    image=$(curl -s "$selected" | grep -Eo "https://cdn.discordapp.com/attachments/[0-9]{18}/[0-9]{18}/[a-zA-Z0-9_-]*.webp" | head -n 1)
    
    w3m "$image"
    
    printf "%s" "Are you sure you want to download (Y/N): " && read -r query
    
    if [[ "$query" == "Y" || "$query" == "y" ]] ; then
        download "$req"
    else
        printf "%s\n" "Exiting..."
    fi
}

main "$url"
