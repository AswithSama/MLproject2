from setuptools import find_packages, setup

def get_requirements(filepath):
    requirements=[]
    with open(filepath) as f:
        requirements=f.readlines()
    for i in requirements:
        i=i.replace('\n','')
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements


setup(
    name='mlproject2',
    version='0.0.1',
    author='Aswith', 
    author_email='samaaswith7@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)