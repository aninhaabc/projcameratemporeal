from setuptools import setup, find_packages
import os

def find_subdir(start_dir):
    # Get the list of all subdirectories starting at the given path
    subdirectories = [x[0] for x in os.walk(start_dir)]
    subdirectories = [x.split('/',1)[-1]+'/*' for x in subdirectories]
    return subdirectories

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

MODULE_STUB = "aps"

setup(
    name=MODULE_STUB,  # Substitua pelo nome do seu pacote   
    version="0.1.0",
    author="Ana Beatriz da Cunha e Manoela Saragoca",
    author_email="anabc1@al.insper.edu.br",
    description="Analise da camera em tempo real",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aninhaabc/projcameratemporeal",  # URL do repositório do seu projeto (se houver)
    packages=find_packages(), # Encontra automaticamente todos os pacotes no diretório
    package_data={
    '': find_subdir(f'{MODULE_STUB}'),
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            f'cameratemporeal={MODULE_STUB}.camera_tempo_real:main',
        ],
    },
    install_requires=[  # Instala as dependências especificadas no requirements.txt
        line.strip() for line in open("requirements.txt").readlines()
    ],

)