from setuptools import setup
import os



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


long_description = read("README.md")

here = os.path.abspath(os.path.dirname(__file__))


setup(
    name='sqlademo',
    version='demo',
    url='http://github.com/jlgoldb2/SQLAlchemy_demo/',
    license='MIT License',
    author='Jason Goldberger',
    tests_require=['pytest'],
    install_requires=['SQLAlchemy==0.9.4'],
    author_email='jlgoldb2@asu.edu',
    description='a simple demonstration for using postgreSQL via SQLAlchemy ORM',
    long_description=long_description,
    packages=['sqlademo'],
    include_package_data=True,
    platforms='any',
    test_suite='sqlademo.test.test_sqlademo',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
        ],
    extras_require={
        'testing': ['pytest'],
    }
)