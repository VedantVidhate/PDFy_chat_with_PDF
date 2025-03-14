from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'

def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

if __name__=="__main__":
    setup(
        name='PDFy: Chat with PDF',
        version='0.1',
        author='Aman Vishwakarma, Arshan Dastur',
        author_email='amansharma1729ds@gmail.com, ',
        install_requires=get_requirements('requirements.txt'),
        packages=find_packages()

    )