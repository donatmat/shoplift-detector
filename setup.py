from setuptools import setup, find_packages

setup(
    name="shoplift-detector",  # Nom de votre projet
    version="1.0.0",  # Numéro de version
    description="Un système de détection des comportements de vol à partir des images de vidéosurveillance dans les supermarchés.",
    author="Votre Nom",  # Remplacez par votre nom
    author_email="votre.email@example.com",  # Remplacez par votre email
    url="https://github.com/votreutilisateur/shoplift-detector",  # Remplacez par l'URL de votre repo GitHub (si disponible)
    packages=find_packages(),  # Recherche automatiquement tous les packages dans votre projet
    install_requires=[
        "numpy",
        "opencv-python",
        "tensorflow>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choisissez une licence appropriée
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Spécifiez la version minimale de Python requise
)
