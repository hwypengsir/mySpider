# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name='mySpider',
    version='1.0',
    packages=find_packages(),
    package_data={
        'mySpider': ['resources/*.txt']
    },
    entry_points={
        'scrapy': ['settings = mySpider.settings']
    },
    zip_safe=False,
)
