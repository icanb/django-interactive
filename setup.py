import codecs
from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


PACKAGE = "interactive"
NAME = "django-interactive"
DESCRIPTION = "Building easier client-side connections"
AUTHOR = "Ilter Canberk, Naman Seth"
AUTHOR_EMAIL = "iltercanberk@gmail.com"
URL = "https://github.com/CMU-Web-Application-Development/Team71"


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=read("README.md"),
    version="1.0.6",
    license="MIT",
    url=URL,
    packages=find_packages(),
    package_data={
        "interactive": [
            "templates/stubs/base_js_stub.template"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    install_requires=[
        "django>=1.7",
        "pyquery==1.2.9"
    ],
    # TODO: Fix this part once we have tests.
    # test_suite="runtests.runtests",
    # tests_require=[
    #     "mock",
    # ],
    zip_safe=False,
)