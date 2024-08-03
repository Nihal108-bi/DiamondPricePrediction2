from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  
        return requirements

setup(
    name='DiamondPricePrediction',
    verson='0.0.1',
    author='Nihal',
    author_email='2207340130034@recbanda.ac.in',
    install_requires=get_requirements('requirements.txt'),     #['pandas','numpy'],
    packages=find_packages()
)