# coding: utf-8

"""
    First Data Gateway RESTFUL API Python SDK

    Python SDK to be used with a First Data Gateway account. 
    This SDK has been created and packaged to offer the easiest way to integrate your application into the First Data Gateway. 
    This SDK gives you the ability to run transactions such as sales, preauthorizations, postauthorizations, credits, voids, 
    and returns; transaction inquiries; setting up scheduled payments and much more.

    OpenAPI spec version: 0.0.1
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "first_data_gateway"
VERSION = "1.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="First Data Gateway RESTFUL API Python SDK",
    author="Eric Margules",
    author_email="eric.margules@firstdata.com",
    url="https://docs.firstdata.com/org/gateway",
    keywords=["Payment", "Gateway", "SDK", "Developer", "First Data"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    license = 'MIT',
    long_description="Python SDK to be used with a First Data Gateway account. This SDK has been created and packaged to offer the easiest way to integrate your application into the First Data Gateway. This SDK gives you the ability to run transactions such as sales, preauthorizations, postauthorizations, credits, voids, and returns; transaction inquiries; setting up scheduled payments and much more."
)
