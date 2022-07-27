from setuptools import setup, find_packages
from artfzf.__version__ import __core__

with open("requirements.txt") as requirements_txt:
    requirements = requirements_txt.read().splitlines()

setup(
        name="artfzf",
        version=__core__,
        author="d3m0n@demonkingswarn",
        author_email="swarn@demonkingswarn.ml",
        description="Download high quality 3D models via the commandline.",
        packages=find_packages(),
        url="https://github.com/DemonicAayush/artfzf",
        keywords=[
            "3D",
            "artgare",
            "fzf",
            "3D models",
            "free"
        ],
        install_requires=requirements,
        entry_points="""
            [console_scripts]
            artfzf=artfzf.__main__:__artfzf__
        """,
        include_package_data=True,
)
