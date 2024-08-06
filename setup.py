from setuptools import setup, find_packages

HYPHEN_DOT_E = "-e ."
# if we have this string appended in the end of  the req.txt file then while installing the requirements
# it will automatically trigger setup.py as well which will help with the package build.

def get_required_libs(file_path:str) -> list[str]:
    libs = []
    with open(file_path,'r') as file_obj:
        libs = file_obj.readlines()
        libs=[x.replace("\n","") for x in libs]
        
        if HYPHEN_DOT_E in libs:
            libs.remove(HYPHEN_DOT_E)
    return libs

setup(
    name = 'mlProject',
    version = '0.0.1',
    author = 'modiChicha',
    packages = find_packages(),
    install_requires =get_required_libs("requirements.txt")
)