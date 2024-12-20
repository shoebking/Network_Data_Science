from setuptools import find_packages,setup
from typing import List

def get_requirements() -> List[str]:

    requirements_list:List[str]=[]

    try:

        with open('requirements.txt','r') as f:

            lines=f.readlines()

            for line in lines:
                requirement=line.strip()
                if(requirement and requirement!='-e .'):
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("File not found")

    return requirements_list

print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shoeb Ahmed",
    author_email="shoebahmed061@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)