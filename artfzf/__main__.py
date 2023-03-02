import httpx
from fzf import fzf_prompt

import re
import subprocess
import platform
import os
import random

headers = {
        "User-Agent": "uwu"
}

client = httpx.Client(headers=headers, follow_redirects=True, timeout=None)

url = "https://artgare.com/3d-library-listing-sitemap.xml"

color = [  
    "\u001b[31m",
    "\u001b[32m",
    "\u001b[33m",
    "\u001b[34m",
    "\u001b[35m",
    "\u001b[36m",
    "\u001b[37m"
]

color_idx = random.randint(0, len(color)-1)

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

    print(f"{color[color_idx]}Downloaded at {path}\u001b[0m")


def __artfzf__():
    resp = client.get(url)
    
    hmmm = re.findall(r'<loc>(.*?)</loc>', resp.text)
    
    selected = fzf_prompt(hmmm)

    if selected == None:
        print(f"{color[color_idx]}[!] Nothing to download.\u001b[0m")
        exit(1)

    req = client.get(selected)

    downloadlink = re.findall(r'href="(https://dl.dropboxusercontent/[a-z]{1}/[a-zA-Z0-9]{15}/.*?)"', req.text)

    show = fzf_prompt(downloadlink, select_first=True)

    path: str = determine_path()
    download(path, show)

if __name__ == "__main__":
    __artfzf__()
