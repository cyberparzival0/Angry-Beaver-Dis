import setuptools

with open("README.md") as _file:
    long_description = _file.read()

setuptools.setup(
        name= "angry_beaver_dis",
        version = "2.3.0",
        author = "Cyber Parzival",
        author_email = "titangrid4@gmail.com",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "",
        packages=setuptools.find_packages(),
        install_requires = [
        ], 
        license = "MIT",
        classifiers =  [
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
        ],
)
