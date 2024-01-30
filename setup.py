# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.1
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "Python Eliona API client 2"
VERSION = "2.6.1"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Eliona REST API",
    author="Eliona by IoTEC AG",
    author_email="hello@eliona.io",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Eliona REST API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT License",
    long_description_content_type='text/markdown',
    long_description="""\
    The Eliona REST API enables unified access to the resources and data of an Eliona environment.
    """,  # noqa: E501
    package_data={"eliona.api_client2": ["py.typed"]},
)
