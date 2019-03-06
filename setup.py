import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ml_testing",
    version="0.1",
    description="Testing for models confirming to the scikit-learn api",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EricSchles/ml_testing",
    author="Eric Schles",
    author_email="ericschles@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ml_test", 'ml_test.classification_tests', 'ml_test.columnar_tests',
              'ml_test.regression_tests', 'ml_test.structural_tests'],
    include_package_data=True,
    install_requires=["sklearn", "scipy", "numpy"],
)
