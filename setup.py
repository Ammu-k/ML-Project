from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    print("Before removing:", requirements)

    requirements = [req for req in requirements if req != HYPHEN_E_DOT]

    print("After removing:", requirements)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    author="Amulya",
    author_email="ammukaranji8@gmail.com",
)