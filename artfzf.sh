#!/bin/sh

url="https://artgare.com"
download_dir="$HOME/Downloads"

selected=$(curl -s "$url" -A "uwu" | tr '<|>' '\n' | sed -nE 's_a href="(.*model/[^"]*)"$_\1_p' | fzf -d'/' --with-nth 5)

[ -z "$selected" ] && printf "%s\n" "[!] Nothing to download" && exit 1

req=$(curl -s "$selected" | tr '<|>' '\n' | sed -nE 's_a href="(.*\.zip[^"]*)".*_\1_p; s_.*content="(.*\.webp[^"]*)".*_\1_p')

w3m "$(printf "%s" "$req" | head -1 )"

printf "%s" "Are you sure you want to download (Y/N): " && read -r query

if [ "$query" = "Y" ] || [ "$query" = "y" ]; then
    aria2c --dir="${download_dir}" "$(printf "%s" "$req" | tail -1)"
else
    printf "%s\n" "Exiting..."
fi
