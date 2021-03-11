import setuptools

setuptools.setup(
    name="postcodes",
    version="1.0.0",
    author="Eugene Lee",
    license="Apache 2.0",
    author_email="eugene.lee@centraliens.net",
    description="Program to query Postcodes API",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests==2.25.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9"
    ],
)