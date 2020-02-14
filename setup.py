import setuptools

setuptools.setup(
    name="spacie",
    version="0.0.1",
    author="William Wyatt",
    author_email="tsangares@gmail.com",
    description="Space sync app",
    long_description="For spacebar syncing.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Tsangares/Spacy",
    include_package_data=True,
    scripts=[
        'spacy/spacy_client.py',
        'spacy/spacy_server.py',
    ],
    install_requires=[
        "MouseInfo==0.1.2",
        "Pillow==7.0.0",
        "PyAutoGUI==0.9.48",
        "PyGetWindow==0.0.8",
        "PyMsgBox==1.0.7",
        "pynput==1.6.6",
        "pyperclip==1.7.0",
        "PyRect==0.1.4",
        "PyScreeze==0.1.26",
        "python-xlib==0.26",
        "python3-xlib==0.15",
        "PyTweening==1.0.3",
        "six==1.14.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
