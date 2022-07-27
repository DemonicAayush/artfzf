<h1 align="center">
  ARTFZF
</h1>
<br>
<h3 align="center">
Download high quality 3D models from the commandline. This tool scrapes the site <a href="https://artgare.com">artgare</a>.
</h3>
<br>

# Install

<i>Install dependencies <a href="https://github.com/DemonicAayush/artfzf#dependencies">(See below)</a></i>

This project can be installed on to your device via different mechanisms, these mechanisms are listed below in the order of ease.

1. PIP Installs packages <b>aka</b> PIP Installation
```sh
pip install git+https://github.com/demonicaayush/artfzf
```

2. Source Code Download
```sh
git clone https://github.com/demonicaayush/artfzf
```
Given that you have [`git`](https://git-scm.com) installed, you can clone this repository from GitHub. If you do not have or want to deal wtih installation of [`git`](https://git-scm.com), you can simply download the repository using <a href="https://gitHub.com/DemonicAayush/artfzf/archive/refs/heads/master.zip">this link</a>.

After the repository is downloaded and placed in an appropriate directory, you can use `setup.py` to proceed with the installation.
```sh
pip install .
```
This command is to be executed from the directory where the repository is located.

# Dependencies
- [`fzf`](https://github.com/junegunn/fzf) - for selection screen.
- [`aria2`](https://github.com/aria2/aria2) - download manager.
