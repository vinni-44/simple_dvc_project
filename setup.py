from setuptools import setup,find_packages

with open("README.md",'r',encoding='utf-8') as f:
    long_discription = f.read()



setup(
    name = 'src',
    version='0.0.1',
    author='vinni-44',
    description='A small package for dvc ml demo',
    long_description=long_discription,
    long_description_content_type='text/markdown',
    url='https://github.com/vinni-44/simple_dvc_project.git',
    package_dir={'':'src'},
    packages=find_packages(where = 'src'),
    license='GNU',
    python_requires = ">=3.9",
    install_requires = ['dvc','dvc[gdrive]','dvc[s3]','pandas','scikit-learn']
    
)