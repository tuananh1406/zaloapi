from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'zaloapi: Zalo API for Python'
LONG_DESCRIPTION = 'Zalo API for Python. This project was inspired by fbchat. No API key is needed. Just use your email and password (Not support yet) or cookies.\n\nDocuments: https://vrxx1337.dev/zaloapi/docs'

# Setting up
setup(
    name="zaloapi",
    version=VERSION,
    author="Lê Quốc Việt (Vexx)",
    author_email="<vrxxdev@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'aenum', 'attr', 'pycryptodome', 'datetime'],
    keywords=['python', 'zalo', 'api', 'zalo api', 'zalo chat', 'requests'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]
)
