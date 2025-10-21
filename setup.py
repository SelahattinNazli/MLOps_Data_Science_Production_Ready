from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_list = []
    try:
        with open('requirements.txt', 'r') as f:
            requirement_list = [req.strip() for req in f.readlines()]
            if '-e .' in requirement_list:
                requirement_list.remove('-e .')
    except FileNotFoundError:
        pass
    return requirement_list

setup(
    name="us_visa",
    version="0.0.1",
    author="selahattin",
    author_email="selahattinnazli3@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.8",
)
