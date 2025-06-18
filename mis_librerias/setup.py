import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'Ambiental'
AUTHOR = 'Daniel Gonzalez ' #Modificar con vuestros datos
AUTHOR_EMAIL = 'danielricardo.gonzalezpolo@gmail.com' #Modificar con vuestros datos
URL = '' #Modificar con vuestros datos

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Librería abordar problemas ambientales a través de la matematicas' #Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,    
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[]
)