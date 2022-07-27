import httpx
from fzf import fzf_prompt

import re
import subprocess
import platform
import os

headers = {
        "User-Agent": "uwu"
}

client = httpx.Client(headers=headers, follow_redirects=True, timeout=None)

url = "https://artgare.com"

def determine_path() -> str:

    plt = platform.system()

    if plt == "Windows":
        return f"C://Users//{os.getenv('username')}//Downloads"

    elif plt == "Linux":
        return f"/home/{os.getlogin()}/Downloads"

    elif plt == "Darwin":
        return f"/Users/{os.getlogin()}/Downloads"

def download(path, link):
    args = [
            "aria2c",
            f"--dir={path}",
            f"{link}"
        ]
    aria2_process = subprocess.Popen(args)
    aria2_process.wait()

    print(f"Downloaded at {path}")


def __artfzf__():
    resp = client.get(url)
    
    hmmm = re.findall(r'https://artgare.com/free-3d-model/[a-zA-Z0-9%-]*/', resp.text)
    #print(hmmm)
    unique_list = []

    for x in hmmm:
        if x not in unique_list:
            unique_list.append(x)

    selected = fzf_prompt(unique_list)

    if selected == None:
        print("[!] Nothing to download.")
        exit(1)

    req = client.get(selected)

    downloadlink = re.findall(r'href="(https://cdn.discordapp.com/.*?)"', req.text)

    show = fzf_prompt(downloadlink, select_first=True)
    #show = show.replace("amp;", "")

    path: str = determine_path()
    download(path, show)

if __name__ == "__main__":
    __artfzf__()
